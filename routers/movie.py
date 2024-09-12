from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List
#IMPORTAR LIBRERIAS DE BD
from config.database import Session
#IMPORTAR LIBRERIA DE MODEL
from models.movie import Movie as MovieModel
#IMPORTAR LIBRERIA DE ENCODER
from fastapi.encoders import jsonable_encoder
#IMPORTAR CLASE DE JWT_BEARER
from middlewares.jwt_bearer import JWTBearer
#IMPORTAR SERVICIOS DE MOVIE
from services.movie import MovieService
#IMPORTAR SCHEMA DE MOVIE
from schemas.movie import Movie

movie_router = APIRouter()

#CRUD DE LAS APIS
#LISTADO DE PELICULAS
@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200 ,content=jsonable_encoder(result))

#LISTADO POR GET BY ID
@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie, status_code=200)
def get_movie(id : int = Path(ge=1, le=2000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movies_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message':"No encontrado"})
    return JSONResponse(status_code=200 ,content=jsonable_encoder(result))

#LISTADO POR CATEGORIA
@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie], status_code=200)
def get_movies_by_category(category : str = Query(min_length=1, max_length=15), year : int = Query(le=2023)) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies_category(category, year)
    if not result:
        return JSONResponse(status_code=404, content={'message':"No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
    #data = [item for item in movies if item["category"] == category and int(item["year"]) == year]
    #return JSONResponse(status_code=200 ,content=data)

#CREACION DE PELICULAS
@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201 ,content={"message":"Se ha creado la pelicula"})

#ACTUALIZACION DE PELICULAS
@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id : int, movie: Movie) -> dict:
    try:
        db = Session()
        MovieService(db).update_movie(id, movie)
        return JSONResponse(status_code=200 ,content={"message":"Se ha modificado la pelicula"})
    except Exception:
        return JSONResponse(status_code=404, content={'message':"No encontrado"})

#ELIMINACION DE PELICULAS
@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id : int) -> dict:
    try:
        db = Session()
        MovieService(db).delete_movie(id)
        return JSONResponse(status_code=200 ,content={"message":"Se ha eliminado la pelicula"})
    except Exception:
        return JSONResponse(status_code=404, content={'message':"No encontrado"})