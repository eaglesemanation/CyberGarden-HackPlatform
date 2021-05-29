import os
import json
import random
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from models import Team, User
from crud.users import get_user
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

router = APIRouter()


class NewTeam(BaseModel):
    name: str


PrivateTeam = pydantic_model_creator(
    Team, exclude=('hackathons', )
)

# print(os.listdir())
with open('crud/words.json', 'r', encoding='utf8') as file:
    words = json.load(file)


@router.post('/create', response_model=PrivateTeam)
async def create(new_team: NewTeam, user=Depends(get_user)):
    invite_link = '-'.join([random.choice(words) for _ in range(5)])
    captain = (await user.as_captain)[0]
    team = await Team.create(capitan_id=captain.id, **new_team.dict(), invite_link=invite_link)
    await team.participants.add(await user.as_participant)
    return await PrivateTeam.from_tortoise_orm(team)


@router.get('/all', response_model=List[PrivateTeam])
async def get_all():
    return await PrivateTeam.from_queryset(Team.all())


@router.get('/enter/{invite_link}', response_model=PrivateTeam)
async def enter(invite_link: str, user=Depends(get_user)):
    team = await Team.get_or_none(invite_link=invite_link)
    if team is None:
        raise HTTPException(status_code=404, detail='Team not found')
    await team.participants.add(await user.as_participant)
    return await PrivateTeam.from_tortoise_orm(team)


@router.delete("/{id}")
async def destroy(id: int):
    team = await Team.get_or_none(id=id)
    if team is None:
        return HTTPException(status_code=404, detail='Hackathon not found')
    await team.delete()
    return {"ok": True}


@router.get('/{id}', response_model=PrivateTeam)
async def get_single(id: int):
    team = await Team.get_or_none(id=id)
    if team is None:
        raise HTTPException(status_code=404, detail='Hackathon not found')
    return await PrivateTeam.from_tortoise_orm(team)
