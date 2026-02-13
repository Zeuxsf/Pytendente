from fastapi import APIRouter
from me_info import responder_me
from demo import responder_demo
from git_api import principais_repos
from tickets import abrir_ticket, visualizar_ticket
from schemas import TicketAbrir, Question


action_router = APIRouter(prefix="/action", tags=["Action"])

@action_router.post("/conversation/me")
async def conversation_me(data: Question):
    return responder_me(data.question)

@action_router.get("/conversation/me/repos")
async def repos():
    return principais_repos()

@action_router.post("/conversation/demo")
async def conversation_demo(data: Question):
    return responder_demo(data.question)

@action_router.post("/tickets/abrir")
async def ticket_abrir(data: TicketAbrir):
    codigo = abrir_ticket(
        data.nome,
        data.user_email,
        data.assunto, 
        data.mensagem)
    return {"codigo": codigo}

@action_router.get("/tickets/visualizar")
async def ticket_visualizar(user_email,codigo):
    return visualizar_ticket(user_email,codigo)
