from sqlmodel import Session, select
from app.db.database import create_db_and_tables, engine
from app.models import Item


def add_example_items():
    create_db_and_tables()

    with Session(engine) as session:
        existing_item = session.exec(select(Item)).first()
        if existing_item is None:
            session.add(Item(name="Item 1", description="Descripción 1"))
            session.add(Item(name="Item 2", description="Descripción 2"))
            session.add(Item(name="Item 3", description="Descripción 3"))
            session.add(Item(name="Item 4", description="Descripción 4"))
            session.add(Item(name="Item 5", description="Descripción 5"))
            session.commit()
            print("Datos de ejemplo agregados a la base de datos.")
        else:
            print("La base de datos ya contiene items. No se agregaron datos de ejemplo.")


if __name__ == "__main__":
    add_example_items()
