from pydantic import BaseModel,Field
from typing import Annotated


class CreateMovieRequest(BaseModel):
    title: str
    playtime: int
    genre: list[str]

class MovieResponse(BaseModel):
    id: int
    title: str
    playtime: int
    genre: list[str]

class MovieUpdateRequest(BaseModel):
    title: str
    playtime: int
    genre: list[str]

class MovieSearchParams(BaseModel):
	title: str | None = None
	genre: str | None = None

