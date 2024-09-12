from fastapi import APIRouter
from fastapi.responses import HTMLResponse

home_router = APIRouter()

@home_router.get('/', tags=['Home'])
def menssage():
    return HTMLResponse('<h1>Hello world MIS OTAKUS DE LAS QUINTIDIOSAS</h1>')