from typing import List

from fastapi import APIRouter, Depends
from models import Hackathon, Team
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

from crud.users import get_participant

router = APIRouter()

Team_Pydantic = pydantic_model_creator(Team)
Teams_Queryset = pydantic_queryset_creator(Team)
Hackathon_Pydantic = pydantic_model_creator(Hackathon)


@router.get("/teams", response_model=List[Team_Pydantic])
async def get_teams(user=Depends(get_participant)):
    participant = await user.as_participant
    return await Team_Pydantic.from_queryset(participant.teams.all())


@router.get("/hackathons", response_model=List[Hackathon_Pydantic])
async def get_hackathons(user=Depends(get_participant)):
    participant = await user.as_participant
    teams = await participant.teams.all()
    hackathons: List[Hackathon_Pydantic] = []
    for team in teams:
        hackathons += await Hackathon_Pydantic.from_queryset(team.hackathons.all())
    return hackathons
