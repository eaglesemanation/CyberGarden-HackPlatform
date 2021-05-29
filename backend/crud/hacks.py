from datetime import date
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from models import Hackathon
from pydantic import BaseModel, Field
from tortoise.contrib.pydantic import pydantic_model_creator

from crud.users import get_user

router = APIRouter()


class NewHackathon(BaseModel):
    name: str
    description: str
    start_date: date = Field(default="2021-05-29")
    end_date: date = Field(default="2021-05-29")


PublicHackathon = pydantic_model_creator(Hackathon, exclude=("organizers", "teams"))
UpdatedHackathon = pydantic_model_creator(
    Hackathon, exclude=("id", "organizers", "teams", "sponsors", "tags")
)


# TODO organizer check
@router.post("/create", response_model=PublicHackathon)
async def create(new_hack: NewHackathon, user=Depends(get_user)):
    hack = await Hackathon.create(**new_hack.dict())
    return await PublicHackathon.from_tortoise_orm(hack)


# TODO organizer check
@router.delete("/{id}")
async def destroy(id: int, user=Depends(get_user)):
    hack = await Hackathon.get_or_none(id=id)
    if hack is None:
        return HTTPException(status_code=404, detail="Hackathon not found")
    await hack.delete()
    return {"ok": True}


@router.get("/all", response_model=List[PublicHackathon])
async def get_all():
    return await PublicHackathon.from_queryset(Hackathon.all())


@router.get("/{id}", response_model=PublicHackathon)
async def get_single(id: int):
    hack = await Hackathon.get_or_none(id=id)
    if hack is None:
        raise HTTPException(status_code=404, detail="Hackathon not found")
    return await PublicHackathon.from_tortoise_orm(hack)


# TODO: organizer check
# TODO: m2m updates
@router.put("/{id}", response_model=PublicHackathon)
async def update_single(id: int, new_hack: UpdatedHackathon, user=Depends(get_user)):
    hack = await Hackathon.get_or_none(id=id)
    if hack is None:
        raise HTTPException(status_code=404, detail="Hackathon not found")
    hack.update_from_dict(new_hack.dict())
    await hack.save()
    return await PublicHackathon.from_tortoise_orm(hack)
