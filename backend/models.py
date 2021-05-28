from tortoise import Model, Tortoise, fields


class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=128, unique=True)
    hashed_password = fields.CharField(max_length=512)

    fio = fields.CharField(null=True, max_length=128)
    is_admin = fields.BooleanField(default=False)

    def __repr__(self):
        return str(self.email)

    class PydanticMeta:
        exclude = ["hashed_password", "is_admin"]


Tortoise.init_models(["models"], "models")
