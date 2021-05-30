from datetime import date
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from httpx import AsyncClient
from models import Hackathon, Publication
from pydantic import BaseModel, Field
from tortoise.contrib.pydantic import pydantic_model_creator

from crud.users import get_capitan, get_organizer, get_user

router = APIRouter()


class NewHackathon(BaseModel):
    name: str
    description: str
    start_date: date = Field(default="2021-05-29")
    end_date: date = Field(default="2021-05-29")
    image: str = Field(
        default="https://cdn22.img.ria.ru/images/07e4/05/06/1571020469_0:0:1920:1080_600x0_80_0_0_8492ea5758147feadb42f576ad3ae00c.jpg"
    )


PublicHackathon = pydantic_model_creator(Hackathon, exclude=("organizers", "teams"))
UpdatedHackathon = pydantic_model_creator(
    Hackathon, exclude=("id", "organizers", "teams", "sponsors", "tags")
)


@router.post("/create", response_model=PublicHackathon)
async def create(new_hack: NewHackathon, user=Depends(get_user)):
    hack = await Hackathon.create(**new_hack.dict())
    await hack.organizers.add(await user.as_organizer)
    return await PublicHackathon.from_tortoise_orm(hack)


@router.delete("/{id}")
async def destroy(id: int, user=Depends(get_organizer)):
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
    print()
    return await PublicHackathon.from_tortoise_orm(hack)


class ParticipantsAmount(BaseModel):
    amount: int


@router.get("/{id}/participants_amount", response_model=ParticipantsAmount)
async def get_participants_amount(id: int):
    hack = await Hackathon.get_or_none(id=id)
    if hack is None:
        raise HTTPException(status_code=404, detail="Hackathon not found")
    amount = await hack.participants_amount()
    return ParticipantsAmount.construct(amount=amount)


# TODO: m2m updates
@router.put("/{id}", response_model=PublicHackathon)
async def update_single(
    id: int, new_hack: UpdatedHackathon, user=Depends(get_organizer)
):
    hack = await Hackathon.get_or_none(id=id)
    if hack is None:
        raise HTTPException(status_code=404, detail="Hackathon not found")
    hack.update_from_dict(new_hack.dict())
    await hack.save()
    return await PublicHackathon.from_tortoise_orm(hack)


@router.post("/enter/{id}", response_model=PublicHackathon)
async def enter_hackathon(id: int, user=Depends(get_capitan)):
    hack = await Hackathon.get_or_none(id=id)
    if hack is None:
        raise HTTPException(status_code=404, detail="Hackathon not found")
    [captain] = await user.as_captain
    await hack.teams.add(await captain.team)
    return await PublicHackathon.from_tortoise_orm(hack)


class NewPublication(BaseModel):
    title: str
    text: str


PublicationView = pydantic_model_creator(Publication, exclude=("hackathon",))


@router.post("/{id}/publish")
async def publish_post(id: int, publication: NewPublication):
    hackathon = await Hackathon.get_or_none(id=id)
    if hackathon is None:
        raise HTTPException(status_code=404, detail="Hackathon not found")

    publication = await Publication.create(
        **publication.dict(), hackathon_id=hackathon.id
    )
    # TODO FETCH TO BOT SERVER
    message = f"{hackathon.name}: {publication.title}\n{publication.text}"
    print(message)
    async with AsyncClient() as client:
        await client.post("http://notifier:8080", json={"message": message})
    return await PublicationView.from_tortoise_orm(publication)
