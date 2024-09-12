from fastapi import FastAPI
#IMPORTAR LIBRERIAS DE BD
from config.database import engine, Base
#IMPORTAR LIBRERIA DE ERRORHANDLER
from middlewares.error_handler import ErrorHandler
#IMPORTAR LA RUTA A USAR
from routers.movie import movie_router
from routers.user import auth_router
from routers.home import home_router

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

#INCLUSION DE MIDDLEWARES
app.add_middleware(ErrorHandler)

#INCLUSION DE LA RUTA DE MOVIE
app.include_router(movie_router)
app.include_router(auth_router)
app.include_router(home_router)

#Ejecutar la BD
Base.metadata.create_all(bind=engine)

#Listado de Peliculas
movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "Sonic The hedgehog",
        "overview": "En una ciudad llamada Grenn Hill, hay un erizo super veloz que recorre el mundo y tiene como proposito...",
        "year": "2020",
        "rating": 9.8,
        "category": "Aventura"
    }
]