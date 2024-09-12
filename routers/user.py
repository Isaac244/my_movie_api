from fastapi import APIRouter
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
#IMPORTAR LIBRERIA SCHEMA
from schemas.user import User

auth_router = APIRouter()

#AUTENTICACION DE USUARIO
@auth_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == 'admin@gmail.com' and user.password == 'admin':
        token: str = create_token(user.model_dump())
    return JSONResponse(status_code=200, content=token)