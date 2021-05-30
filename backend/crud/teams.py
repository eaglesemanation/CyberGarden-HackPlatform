import json
import random
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from models import Team
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from crud.users import UserRole, get_user

router = APIRouter()
PrivateTeam = pydantic_model_creator(Team, exclude=("hackathons",))


class NewTeam(BaseModel):
    name: str


class MyTeams(BaseModel):
    as_captain: List[PrivateTeam]
    as_participant: List[PrivateTeam]


# print(os.listdir())
with open("crud/words.json", "r", encoding="utf8") as file:
    words = json.load(file)


@router.post("/create", response_model=PrivateTeam)
async def create(new_team: NewTeam, user=Depends(get_user)):
    invite_link = "-".join([random.choice(words) for _ in range(5)])
    user.update_from_dict(dict(role=UserRole.CAPTAIN))
    await user.save()
    captain = await user.as_captain
    team = await Team.create(
        capitan=captain, **new_team.dict(), invite_link=invite_link
    )
    await team.participants.add(await user.as_participant)
    return await PrivateTeam.from_tortoise_orm(team)


@router.get("/my", response_model=MyTeams)
async def my_teams(user=Depends(get_user)):
    captain = await user.as_captain
    participant = await user.as_participant
    as_captain = await PrivateTeam.from_queryset(captain.teams.all())
    as_participant = await PrivateTeam.from_queryset(participant.teams.all())
    return MyTeams(as_captain=as_captain, as_participant=as_participant)


@router.get("/all", response_model=List[PrivateTeam])
async def get_all():
    return await PrivateTeam.from_queryset(Team.all())


@router.get("/enter/{invite_link}", response_model=PrivateTeam)
async def enter(invite_link: str, user=Depends(get_user)):
    team = await Team.get_or_none(invite_link=invite_link)
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    await team.participants.add(await user.as_participant)
    return await PrivateTeam.from_tortoise_orm(team)


@router.delete("/{id}")
async def destroy(id: int):
    team = await Team.get_or_none(id=id)
    if team is None:
        return HTTPException(status_code=404, detail="Team not found")
    await team.delete()
    return {"ok": True}


@router.get("/{id}", response_model=PrivateTeam)
async def get_single(id: int):
    team = await Team.get_or_none(id=id)
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return await PrivateTeam.from_tortoise_orm(team)
