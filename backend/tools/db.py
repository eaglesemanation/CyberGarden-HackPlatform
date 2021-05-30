import json

from models import Hackathon, Location

with open("tools/data.json", "r", encoding="utf8") as file:
    data = json.load(file)


async def fill_db():
    if len(await Hackathon.all()) != 0:
        return
    for hack in data:
        city = hack["city"]
        [location, _] = await Location.get_or_create(city=city)
        del hack["city"]

        await Hackathon.create(
            **hack,
            start_date="2021-05-29",
            end_date="2021-05-29",
            location=location
        )
