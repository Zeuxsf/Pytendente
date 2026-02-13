from pydantic import BaseModel

class TicketAbrir(BaseModel):
    nome: str
    user_email: str
    assunto: str
    mensagem: str

class Question(BaseModel):
    question: str    