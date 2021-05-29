#!/usr/bin/env python

import os
import shutil
from pathlib import Path

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from crud import users, hacks, teams

load_dotenv()

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
app.include_router(hacks.router, prefix='/hacks', tags=["Hacks"])
app.include_router(teams.router, prefix='/teams', tags=["Teams"])

db_url = os.getenv("DB_URL")
config_var = {
    "connections": {"default": db_url},
    "apps": {
        "models": {
            "models": ["models"],
            "default_connection": "default",
        },
    },
}

try:
    shutil.rmtree(
        "db/test"
    )  # Удаляем папку с тестовой базой данных при запуске и импорте

except FileNotFoundError:
    print('Error during delete')
    pass

for path in ["db/test"]:
    Path(path).mkdir(parents=True, exist_ok=True)


@app.on_event("startup")
async def startup():
    await Tortoise.init(config=config_var)
    await Tortoise.generate_schemas(safe=True)


@app.on_event('shutdown')
async def shutdown():
    await Tortoise.close_connections()

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, use_colors=True)
