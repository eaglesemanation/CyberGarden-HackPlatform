from enum import Enum

from tortoise import Model, Tortoise, fields


class UserType(str, Enum):
    participant = "participant"
    capitan = "capitan"
    organizer = "organizer"
    admin = "admin"


class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=128, unique=True)
    hashed_password = fields.CharField(max_length=512)
    fio = fields.CharField(null=True, max_length=128)
    type = fields.CharEnumField(UserType, default=UserType.participant)

    def __repr__(self):
        return str(self.email)

    class PydanticMeta:
        exclude = ["hashed_password"]


class Team(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=128)
    teammates: fields.ManyToManyRelation[User] = fields.ManyToManyField(
        "models.User", related_name="team"
    )

    def __repr__(self):
        return str(self.name)


class Hackathon(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=128)
    description = fields.TextField()
    image_url = fields.CharField(max_length=128)
    teams: fields.ManyToManyRelation[Team] = fields.ManyToManyField(
        "models.Team", related_name="hackathons"
    )

    def __repr__(self):
        return str(self.name)


Tortoise.init_models(["models"], "models")
