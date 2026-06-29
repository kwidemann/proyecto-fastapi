from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from sqlmodel import Session, select
from app.db.database import get_session

from app.models import Item, ItemUpdate

router = APIRouter(prefix="/items", tags=["Items"])

items_db: list[Item] = []

@router.get("/", response_model=List[Item])
def read_items(
    limit: int = Query(10, ge=0),
    offset: int = Query(0, ge=0),
    session: Session = Depends(get_session),
):
    statement = select(Item).offset(offset).limit(limit)
    items = session.exec(statement).all()
    return items

@router.put("/{item_id}", response_model=Item)
def update_item(
    item_id: int, 
    item_update: ItemUpdate,
    session: Session = Depends(get_session),
):
    statement = select(Item).where(Item.id == item_id)
    existing_item = session.exec(statement).first()
    if existing_item is None:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    
    item_data = item_update.model_dump(exclude_unset=True)
    for key, value in item_data.items():
        setattr(existing_item, key, value)

    session.add(existing_item)
    session.commit()
    session.refresh(existing_item)
    return existing_item