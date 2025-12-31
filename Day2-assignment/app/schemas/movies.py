from pydantic import BaseModel


class CreateMovieRequest(BaseModel):
    title: str
    playtime: int
    genre: list[str]

class MovieUpdateRequest(BaseModel):
    title: str
    playtime: int
    genre: list[str]

