#!/usr/bin/env python

import shutil
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from crud import hacks, locations, participants, teams, users
from settings import PROD_TORTOISE_ORM
from tools.db import fill_db

# from backend.tools.db import fill_db


app = FastAPI(
    version="0.0.2",
    title="CyberGarden-HackPlatform",
    description="CyberGarden Hackathon project API based on FastAPI",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(participants.router, prefix="/participants", tags=["Participants"])
app.include_router(hacks.router, prefix="/hacks", tags=["Hacks"])
app.include_router(teams.router, prefix="/teams", tags=["Teams"])
app.include_router(locations.router, prefix="/locations", tags=["Locations"])


try:
    shutil.rmtree(
        "db/test"
    )  # Удаляем папку с тестовой базой данных при запуске и импорте

except FileNotFoundError:
    print("Error during delete")
    pass

for path in ["db/test"]:
    Path(path).mkdir(parents=True, exist_ok=True)

config_var = PROD_TORTOISE_ORM
# config_var = TEST_TORTOISE_ORM

for path in ["db/test", "db/prod"]:
    Path(path).mkdir(parents=True, exist_ok=True)


@app.on_event("startup")
async def startup():
    await Tortoise.init(config=config_var)
    await Tortoise.generate_schemas(safe=True)
    await fill_db()


@app.on_event("shutdown")
async def shutdown():
    await Tortoise.close_connections()


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, use_colors=True)
