# app/crud.py

def create_sample_contact(db: Session):
    contact = Contact(
        name="Ishwari Kape",
        email="ishwarikape@example.com",
        phone="9876543210",
        addresses=[
            Address(street="MG Road", city="Pune", state="Maharashtra", pin_code="411001"),
            Address(street="Link Road", city="Mumbai", state="Maharashtra", pin_code="400001")
        ]
    )
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact
