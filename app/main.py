from fastapi import FastAPI
from app.database.database import engine, Base

from app.models import User

from app.routers.user import router as user_router
from app.routers.auth import router as auth_router

app = FastAPI()
app.include_router(user_router)
app.include_router(auth_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}