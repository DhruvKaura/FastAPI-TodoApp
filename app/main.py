from fastapi import FastAPI
from app.database.database import engine, Base

from app.models import User

from app.routers.user import router as user_router

app = FastAPI()
app.include_router(user_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}