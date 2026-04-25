from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from src.models.repositories.users_repository import UsersRepository

# api router e responsavel por criar rotas

users_routes = APIRouter(tags=["Users"])
# A tag serve pra organizar a documentação automática que o FastAPI gera.

class UpdateUserBody(BaseModel):
    user_name: Optional[str] = None
    age: Optional[int] = None
    uf: Optional[str] = None

@users_routes.post("/users")
async def create_user():
    return JSONResponse(
        content={"Ola": "Mundo"},
        status_code=200
    )

@users_routes.get("/users")
async def get_users(user_name: str):
    repository = UsersRepository()
    users = await repository.get_users_by_name(user_name)
    return JSONResponse(
        content={"users": users},
        status_code=200
    )

@users_routes.put("/users/{user_id}")
async def update_user(user_id: int, body: UpdateUserBody):
    user_infos = body.model_dump(exclude_none=True)
    repository = UsersRepository()
    await repository.update_user(user_id, user_infos)
    return JSONResponse(
        content={"message": "Usuario atualizado com sucesso"},
        status_code=200
    )