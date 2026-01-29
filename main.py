from fastapi import FastAPI
from action_routes import action_router

app = FastAPI()

app.include_router(action_router)