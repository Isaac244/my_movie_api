from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3, max_length=30)
    overview: str = Field(min_length=15, max_length=150)
    year: int = Field(le=2022)
    rating: float =Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=15)

    #Validacion por defecto
    class Config:
        json_schema_extra = {
            "example": {
                "id": 5,
                "title": "Mi pelicula",
                "overview": "Este sera una de las mejores peliculas de wifus",
                "year": 2022,
		        "rating": 9.8,
		        "category": "Acción"
            }
        }
