# Pydantic models

from typing import List

from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    # This Config class is used to provide configurations to Pydantic
    class Config:
        # orm_mode will tell the Pydantic model to read the data even if it is not a dict,
        # but an ORM model (or any other arbitrary object with attributes)
        orm_mode = True
        # With ORM mode, Pydantic will try to access the data it needs from attributes (instead of assuming a dict)


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True



