from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey, JSON
from sqlalchemy.orm import declarative_base, sessionmaker

database = create_engine("sqlite:///data.db")
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

class Log(Base):
    __tablename__ = "logs"

    id = Column("id", Integer,primary_key=True, autoincrement=True)
    question = Column("question", String)
    type_info = Column('type_info', String)
    revised = Column("revised", String, default="No")

    def __init__(self,question,type_info,revised="No"):
        self.question = question
        self.type_info = type_info
        self.revised = revised
