from pydantic import BaseModel
from typing import List

class AddressBase(BaseModel):
    address_line: str
    city: str
    pin_code: str

class ContactCreate(BaseModel):
    name: str
    email: str
    phone: str
    addresses: List[AddressBase]

class ContactOut(ContactCreate):
    id: int
    class Config:
        orm_mode = True
