from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import field_validator, ConfigDict


class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None


class ItemUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None


class Usuario(SQLModel, table=True):
    model_config = ConfigDict(validate_assignment=True)
    
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    email: str

    @field_validator("email")
    @classmethod
    def email_must_contain_at(cls, v: str) -> str:
        if "@" not in v:
            raise ValueError("Email debe contener @")
        return v

    @field_validator("nombre")
    @classmethod
    def nombre_min_length(cls, v: str) -> str:
        if len(v) < 3:
            raise ValueError("Nombre debe tener al menos 3 caracteres")
        return v