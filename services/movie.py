from models.movie import Movie as MovieModel
from schemas.movie import Movie

class MovieService():

    def __init__(self, db) -> None:
        self.db = db

    #LISTADO DE MOVIE
    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    
    #LISTADO DE MOVIE POR ID
    def get_movies_id(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    
    #LISTADO DE MOVIE POR QUERY
    def get_movies_category(self, category, year):
        result = self.db.query(MovieModel).filter(MovieModel.category == category, MovieModel.year == year).all()
        return result
    
    #CREACION DE MOVIE
    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.model_dump())
        self.db.add(new_movie)
        self.db.commit()
        return
    
    #ACTUALIZACION DE MOVIE
    def update_movie(self, id: int, data: Movie):
        movie = self.get_movies_id(id)
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()
        return
    
    #ELIMINAR MOVIE
    def delete_movie(self, id: int):
        self.db.query(MovieModel).filter(MovieModel.id == id).delete()
        self.db.commit()
        return