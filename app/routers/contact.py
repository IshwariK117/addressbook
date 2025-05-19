from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter()  # ✅ Define the router

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/contacts/")
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    db_contact = models.Contact(
        name=contact.name,
        email=contact.email,
        phone=contact.phone,
    )
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)

    for addr in contact.addresses:
        db_address = models.Address(
            contact_id=db_contact.id,
            address_line=addr.address_line,
            city=addr.city,
            pincode=addr.pin_code
        )
        db.add(db_address)
    db.commit()
    return {"message": "Contact created", "data": contact}

@router.get("/contacts/{contact_id}")
def get_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if not contact:
        return {"error": "Contact not found"}
    return {
        "name": contact.name,
        "email": contact.email,
        "phone": contact.phone,
        "addresses": [
            {
                "address_line": addr.address_line,
                "city": addr.city,
                "pin_code": addr.pincode
            }
            for addr in contact.addresses
        ]
    }
