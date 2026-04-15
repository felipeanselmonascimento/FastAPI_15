from fastapi import APIRouter
from fastapi.responses import JSONResponse

# api router e responsavel por criar rotas 

users_routes = APIRouter(tags=["Users"])   
# A tag serve pra organizar a documentação automática que o FastAPI gera.

@users_routes.post("/users")
async def create_user():
    return JSONResponse(
        content={"Ola": "Mundo"},
        status_code=200
    )