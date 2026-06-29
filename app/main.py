from fastapi import FastAPI
from sqlmodel import Session, select
from app.routers.items import router as items_router
from app.db.database import create_db_and_tables, engine
from app.models import Item

app = FastAPI(title="Curso de FastAPI", version="1.0.0")

create_db_and_tables()

app.include_router(items_router)


