from fastapi import APIRouter
from me_info import responder_me
from demo import responder_demo
from git_api import principais_repos
from tickets import abrir_ticket, visualizar_ticket, responder_ticket
from schemas import TicketAbrir, Question, TicketResponder 


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
    return abrir_ticket(data.nome, data.user_email, data.assunto, data.mensagem)

@action_router.get("/tickets/visualizar")
async def ticket_visualizar(user_email, codigo):
    return visualizar_ticket(user_email,codigo)

@action_router.patch("/tickets/responder")
async def ticket_responder(data: TicketResponder):
    return responder_ticket(data.ticket,data.senha,data.resposta)