from enum import Enum

from tortoise import Model, Tortoise, fields


class UserType(str, Enum):
    PARTICIPANT = "participant"
    CAPTAIN = "captain"
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
    as_captain: fields.ReverseRelation["Captain"]
    as_organizer: fields.ReverseRelation["Organizer"]
    as_admin: fields.ReverseRelation["Admin"]

    def __repr__(self):
        return str(self.email)

    class PydanticMeta:
        exclude = ["hashed_password"]


class Participant(Model):
    id = fields.IntField(pk=True)
    user = fields.OneToOneField("models.User", related_name="as_participant")
    teams: fields.ManyToManyRelation["Team"]


class Captain(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="as_captain")
    teams: fields.ForeignKeyRelation["Team"]


class Organizer(Model):
    id = fields.IntField(pk=True)
    user = fields.OneToOneField("models.User", related_name="as_organizer")
    hackathons: fields.ForeignKeyRelation["Hackathon"]


class Admin(Model):
    id = fields.IntField(pk=True)
    user = fields.OneToOneField("models.User", related_name="as_admin")


class Team(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=128)
    participants: fields.ManyToManyRelation[Participant] = fields.ManyToManyField(
        "models.Participant"
    )
    invite_link = fields.CharField(max_length=64, unique=True, allows_generated=True)
    capitan = fields.ForeignKeyField("models.Captain", related_name="")
    hackathons: fields.ManyToManyRelation["Hackathon"]

    def __repr__(self):
        return str(self.name)


class Sponsor(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=128)
    link = fields.CharField(max_length=128)
    image = fields.CharField(max_length=128)
    hackathons: fields.ManyToManyRelation["Hackathon"]


class HackathonTag(Model):
    """Tags to identify type of hackathon, for example: Web, VR, AR, etc"""

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=128)
    hackathons: fields.ManyToManyRelation["Hackathon"]


class Location(Model):
    id = fields.IntField(pk=True)
    city = fields.CharField(max_length=128, null=True)
    hackathon: fields.ForeignKeyRelation["Hackathon"]


class Hackathon(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=128)
    description = fields.TextField()
    start_date = fields.DatetimeField()
    #: Hackathon website url
    image = fields.CharField(max_length=128, null=True)
    url = fields.CharField(max_length=128, null=True)
    location_lon = fields.FloatField(null=True)
    location_lat = fields.FloatField(null=True)
    location = fields.ForeignKeyField("models.Location", related_name="hackathons")
    sponsors: fields.ManyToManyRelation["Sponsor"] = fields.ManyToManyField(
        "models.Sponsor", related_name="hackathons"
    )
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
