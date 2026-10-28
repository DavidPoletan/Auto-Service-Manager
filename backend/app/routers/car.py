from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.schemas.car import Car, CarCreate, CarUpdate
from backend.app.crud.car import (
    get_car,
    get_all_cars,
    create_car,
    update_car,
    delete_car as delete_car_record
)

router = APIRouter()

@router.get("/car/{id}", response_model=Car)
def read_car(id: int, db: Session = Depends(get_db)):
    car = get_car(db, id)

    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")

    return car


@router.get("/", response_model=List[Car])
def read_cars(first_n: Optional[int] = None, db: Session = Depends(get_db)):
    cars = get_all_cars(db)
    return cars[:first_n] if first_n else cars


@router.post("/car/{id}", response_model=Car)
def add_car(car: CarCreate, db: Session = Depends(get_db)):
    return create_car(db, car)


@router.put("/car/{id}", response_model=Car)
def put_car(id: int, car: CarUpdate, db: Session = Depends(get_db)):
    updated_car = update_car(db, id, car)

    if updated_car is None:
        raise HTTPException(status_code=404, detail="Car not found")

    return updated_car


@router.delete("/car/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_car(id: int, db: Session = Depends(get_db)) -> None:
    deleted = delete_car_record(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Car not found")