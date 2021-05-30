from typing import List, Optional

import httpx
from fastapi import APIRouter, HTTPException
from models import Location
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

router = APIRouter()

Location_Pydantic = pydantic_model_creator(Location)


class Coordinate(BaseModel):
    lon: Optional[float]
    lat: Optional[float]


async def get_address(lon, lat):
    resp = httpx.get(
        "https://nominatim.openstreetmap.org/reverse",
        params={"lat": lat, "lon": lon, "zoom": 18, "format": "json"},
    )
    return resp.json()["address"]


async def get_city(coord: Coordinate):
    if coord.lon is not None and coord.lat is not None:
        address = await get_address(coord.lon, coord.lat)
        return address["city"]
    else:
        return "Online"


async def add_city(coord: Coordinate):
    """Searches for city based on location and if it doesn't exist - adds it"""
    city = await get_city(coord)
    [location, _] = await Location.get_or_create(city=city)
    return await Location_Pydantic.from_tortoise_orm(location)


@router.get("/all", response_model=List[Location_Pydantic])
async def all_locations():
    return await Location_Pydantic.from_queryset(Location.all())


@router.get("/{id}", response_model=Location_Pydantic)
async def location(id):
    location = await Location.get_or_none(id=id)
    if location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return await Location_Pydantic.from_tortoise_orm(location)


@router.post("/create", response_model=Location_Pydantic)
async def add_location(coord: Coordinate):
    return await add_city(coord)
