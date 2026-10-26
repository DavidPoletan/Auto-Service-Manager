from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.schemas.customer import Customer, CustomerCreate, CustomerUpdate
from backend.app.crud.customer import (
    get_customer,
    get_all_customers,
    create_customer,
    update_customer,
    delete_customer as delete_customer_record
)

router = APIRouter()

@router.get("/customer/{id}", response_model=Customer)
def read_customer(id: int, db: Session = Depends(get_db)):
    customer = get_customer(db, id)

    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    return customer


@router.get("/", response_model=List[Customer])
def read_customers(first_n: Optional[int] = None, db: Session = Depends(get_db)):
    customers = get_all_customers(db)
    return customers[:first_n] if first_n else customers


@router.post("/customer/{id}", response_model=Customer)
def add_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(db, customer)


@router.put("/customer/{id}", response_model=Customer)
def put_customer(id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    updated_customer = update_customer(db, id, customer)

    if updated_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    return updated_customer


@router.delete("/customer/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(id: int, db: Session = Depends(get_db)) -> None:
    deleted = delete_customer_record(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Customer not found")