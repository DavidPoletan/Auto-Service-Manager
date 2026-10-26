from sqlalchemy.orm import Session
from backend.app.models.customer import Customer
from backend.app.schemas.customer import CustomerCreate, CustomerUpdate

def get_customer(db: Session, id: int):
    return db.get(Customer, id)


def get_all_customers(db: Session):
    return db.query(Customer).all()


def create_customer(db: Session, customer: CustomerCreate):
    db_customer = Customer(
        first_name=customer.first_name,
        last_name=customer.last_name,
        phone=customer.phone,
        email=customer.email,
        address=customer.address
    )

    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)

    return db_customer


def update_customer(db: Session, id: int, customer: CustomerUpdate):
    db_customer = db.get(Customer, id)

    if db_customer is None:
        return None

    for field, value in customer.model_dump(exclude_unset=True, exclude={"updated_at"}).items():
        setattr(db_customer, field, value)

    db.commit()
    db.refresh(db_customer)

    return db_customer


def delete_customer(db: Session, id: int):
    db_customer = db.get(Customer, id)

    if db_customer is None:
        return False

    db.delete(db_customer)
    db.commit()

    return True