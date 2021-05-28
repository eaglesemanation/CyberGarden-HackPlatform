#!/usr/bin/env python

import shutil
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from crud import users
from settings import PROD_TORTOISE_ORM

app = FastAPI(
    version="0.0.1",
    title="CyberGarden-HackPlatform-API",
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

# config_var = TEST_TORTOISE_ORM
config_var = PROD_TORTOISE_ORM

try:
    shutil.rmtree(
        "db/test"
    )  # Удаляем папку с тестовой базой данных при запуске и импорте
except FileNotFoundError:
    pass

for path in ["db/test", "db/prod"]:
    Path(path).mkdir(parents=True, exist_ok=True)


@app.on_event("startup")
async def startup():
    await Tortoise.init(config=config_var)
    await Tortoise.generate_schemas(safe=True)


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, use_colors=True)
