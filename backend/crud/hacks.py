from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from models import Hackathon, User
from crud.users import get_user
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

router = APIRouter()

NewHackathon = pydantic_model_creator(
    Hackathon, include=('name', 'description', 'start_date')
)
PublicHackathon = pydantic_model_creator(
    Hackathon, exclude=('organizers', 'teams')
)


# TODO organizer check
@router.post('/create', response_model=PublicHackathon)
async def create(new_hack: NewHackathon, user=Depends(get_user)):
    hack = await Hackathon.create(**new_hack.dict())
    return await PublicHackathon.from_tortoise_orm(hack)


# TODO organizer check
@router.delete("/{id}")
async def destroy(id: int, user=Depends(get_user)):
    hack = await Hackathon.get_or_none(id=id)
    if hack is None:
        return HTTPException(status_code=404, detail='Hackathon not found')
    await hack.delete()
    return {"ok": True}


@router.get('/all', response_model=List[PublicHackathon])
async def get_all():
    return await PublicHackathon.from_queryset(Hackathon.all())


@router.get('/{id}', response_model=PublicHackathon)
async def get_single(id: int):
    hack = await Hackathon.get_or_none(id=id)
    if hack is None:
        raise HTTPException(status_code=404, detail='Hackathon not found')
    return await PublicHackathon.from_tortoise_orm(hack)
