from fastapi import FastAPI, HTTPException, Path
from typing import Annotated
from fastapi import Query
from app2.models.users import UserModel
from app2.models.movies import MovieModel
from app2.schemas.movies import (
    CreateMovieRequest,
    MovieUpdateRequest,
    MovieResponse,
    MovieSearchParams,
)

app = FastAPI()

UserModel.create_dummy()
MovieModel.create_dummy()

@app.post('/movies', response_model=MovieResponse, status_code=201)
async def create_movie(data: CreateMovieRequest):
	movie = MovieModel.create(**data.model_dump())
	return movie

@app.get("/movies", response_model=list[MovieResponse], status_code=200)
async def get_movies(query_params: Annotated[MovieSearchParams, Query()]):
    valid_query = {
        key: value
        for key, value in query_params.model_dump().items()
        if value is not None
    }

    if valid_query:
        return MovieModel.filter(**valid_query)

    return MovieModel.all()

@app.get('/movies/{movie_id}', response_model=MovieResponse, status_code=200)
async def get_movie(movie_id: int = Path(gt=0)):
	movie = MovieModel.get(id=movie_id)
	if movie is None:
		raise HTTPException(status_code=404)
	return movie

@app.patch('/movies/{movie_id}', response_model=MovieResponse, status_code=200)
async def edit_movie(data: MovieUpdateRequest, movie_id: int = Path(gt=0)):
	movie = MovieModel.get(id=movie_id)
	if movie is None:
		raise HTTPException(status_code=404)
	movie.update(**data.model_dump())
	return movie

@app.delete('/movies/{movie_id}', status_code=204)
async def delete_movie(movie_id: int = Path(gt=0)):
	movie = MovieModel.get(id=movie_id)
	if movie is None:
		raise HTTPException(status_code=404)
	movie.delete()
	return


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
