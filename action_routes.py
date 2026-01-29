from fastapi import APIRouter

action_router = APIRouter(prefix="/action", tags=["Action"])

@action_router.get("nome")
async def nome():
    return "Meu nome"