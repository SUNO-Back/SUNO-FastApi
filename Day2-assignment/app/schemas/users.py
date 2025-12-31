from enum import Enum

from pydantic import BaseModel


class GenderEnum(str, Enum):
    male = "male"
    female = "female"


class UserCreateRequest(BaseModel):
    username: str
    age: int
    gender: GenderEnum
