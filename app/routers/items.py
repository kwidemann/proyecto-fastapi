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

@router.post("/", response_model=Item)
def create_item(
    item: Item,
    session: Session = Depends(get_session),
):
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

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

@router.get("/search", response_model=List[Item])
def search_items(
    name: str = Query(..., description="Nombre a buscar (contiene)"),
    sort: str = Query("asc", description="Orden: asc o desc"),
    limit: int = Query(10, ge=0),
    offset: int = Query(0, ge=0),
    session: Session = Depends(get_session),
):
    # Buscar items que contengan el nombre (case-insensitive)
    statement = select(Item).where(Item.name.ilike(f"%{name}%"))
    
    # Aplicar ordenamiento
    if sort == "desc":
        statement = statement.order_by(Item.name.desc())
    else:
        statement = statement.order_by(Item.name.asc())
    
    # Aplicar paginación
    statement = statement.offset(offset).limit(limit)
    
    items = session.exec(statement).all()
    return items

@router.get("/{item_id}", response_model=Item)
def read_item(
    item_id: int,
    session: Session = Depends(get_session),
):
    statement = select(Item).where(Item.id == item_id)
    item = session.exec(statement).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return item

@router.delete("/{item_id}")
def delete_item(
    item_id: int,
    session: Session = Depends(get_session),
):
    statement = select(Item).where(Item.id == item_id)
    item = session.exec(statement).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    
    session.delete(item)
    session.commit()
    return {"message": "Item eliminado correctamente"}