import uuid

from pydantic import BaseModel, EmailStr, Field, SecretStr


def id_generator():
    return str(uuid.uuid4())

class User(BaseModel):
    id: str = Field(default_factory=id_generator)
    name: str
    email: EmailStr
    password: SecretStr
