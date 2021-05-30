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
            description="""
                Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
                when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
                It has survived not only five centuries, but also the leap into electronic typesetting, 
                remaining essentially unchanged. It was popularised in the 1960s with the release of 
                Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing 
                software like Aldus PageMaker including versions of Lorem Ipsum
            """,
            start_date="2021-05-29",
            end_date="2021-05-29",
            location=location
        )
