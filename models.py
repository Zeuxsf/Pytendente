from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

database = create_engine("sqlite:///dados.db")
Base = declarative_base()

class Client(Base):
    __tablename__ = "clients"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    email = Column("email", String)
    subject = Column("subject", String)
    response = Column("response", String, default="Pendent")

    def __init__(self,name,email,subject,response="Pendent"):
        self.name = name
        self.email = email
        self.subject = subject
        self.response = response
        