from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

database = create_engine("sqlite:///dados.db")
Base = declarative_base()
SessionLocal = sessionmaker(bind=database)

class Client(Base):
    __tablename__ = "clients"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    email = Column("email", String)

    def __init__(self,name,email):
        self.name = name
        self.email = email

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column("id", Integer,primary_key=True,autoincrement=True)
    client_id = Column("client_id", Integer, ForeignKey("clients.id"))
    ticket = Column("ticket", String)
    subject = Column("subject", String)
    response = Column("response", String, default="Pendent")

    def __init__(self,client_id,ticket,subject,response="Pendent"):
        self.client_id = client_id
        self.ticket = ticket
        self.subject = subject
        self.response = response       

