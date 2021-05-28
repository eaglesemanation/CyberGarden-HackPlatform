from enum import Enum

from tortoise import Model, Tortoise, fields


class UserType(str, Enum):
    PARTICIPANT = "participant"
    ORGANIZER = "organizer"
    ADMIN = "admin"


class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=128, unique=True)
    hashed_password = fields.CharField(max_length=512)
    fio = fields.CharField(null=True, max_length=128)
    type = fields.CharEnumField(UserType, default=UserType.PARTICIPANT)
    avatar = fields.CharField(max_length=128, null=True)

    as_participant: fields.ReverseRelation["Participant"]
    as_organizer: fields.ReverseRelation["Organizer"]
    as_admin: fields.ReverseRelation["Admin"]

    def __repr__(self):
        return str(self.email)

    class PydanticMeta:
        exclude = ["hashed_password"]


class Participant(Model):
    id = fields.IntField(pk=True)
    user = fields.OneToOneField("models.User", related_name="as_participant")
    captain: fields.ForeignKeyRelation["Captain"]


class Captain(Model):
    id = fields.IntField(pk=True)
    participant = fields.ForeignKeyField("models.Participant", related_name="captain")
    team = fields.ForeignKeyField("models.Team", related_name="capitan")


class Organizer(Model):
    id = fields.IntField(pk=True)
    user = fields.OneToOneField("models.User", related_name="as_organizer")
    hackathons: fields.ManyToManyRelation["Hackathon"]


class Admin(Model):
    id = fields.IntField(pk=True)
    user = fields.OneToOneField("models.User", related_name="as_admin")


class Team(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=128)
    participants: fields.ManyToManyRelation[Participant] = fields.ManyToManyField(
        "models.Participant"
    )
    capitan: fields.ForeignKeyRelation["Captain"]
    hackathons: fields.ManyToManyRelation["Hackathon"]

    def __repr__(self):
        return str(self.name)


class HackathonTag(Model):
    """Tags to identify type of hackathon, for example: Web, VR, AR, etc"""

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=128)
    hackathons: fields.ManyToManyRelation["Hackathon"]


class Hackathon(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=128)
    description = fields.TextField()
    image_url = fields.CharField(max_length=128, null=True)
    #: Hackathon website url
    url = fields.CharField(max_length=128, null=True)
    start_date = fields.DatetimeField()
    location_longtitude = fields.FloatField(null=True)
    location_latitude = fields.FloatField(null=True)
    teams: fields.ManyToManyRelation[Team] = fields.ManyToManyField(
        "models.Team", related_name="hackathons"
    )
    tags: fields.ManyToManyRelation[HackathonTag] = fields.ManyToManyField(
        "models.HackathonTag", related_name="hackathons"
    )
    organizers: fields.ManyToManyRelation[Organizer] = fields.ManyToManyField(
        "models.Organizer", related_name="hackathons"
    )

    def __repr__(self):
        return str(self.name)


Tortoise.init_models(["models"], "models")
