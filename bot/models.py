from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey, JSON
from sqlalchemy.orm import declarative_base, sessionmaker

database = create_engine("sqlite:///knowledge.db")
Base = declarative_base()
SessionLocal = sessionmaker(bind=database)

class Me_Info(Base):
    __tablename__ = "me_info"

    id = Column("id", Integer,primary_key=True, autoincrement=True)
    question = Column("question", JSON)
    response = Column("response", String)

    def __init__(self, question,response):
        self.question = question
        self.response = response

class Enterprise_Info(Base):
    __tablename__ = "enterprise_info"

    id = Column("id", Integer,primary_key=True, autoincrement=True)
    question = Column("question", JSON)
    response = Column("response", String)

    def __init__(self, question,response):
        self.question = question
        self.response = response
