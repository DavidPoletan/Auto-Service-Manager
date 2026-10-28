from sqlalchemy.orm import Session
from backend.app.models.car import Car
from backend.app.schemas.car import CarCreate, CarUpdate

def get_car(db:Session, id: int):
    return db.get(Car, id)


def get_all_cars(db: Session):
    return db.query(Car).all()


def create_car(db: Session, car: CarCreate):
    db_car = Car(
        customer_id=car.customer_id,
        brand=car.brand,
        model=car.model,
        year=car.year,
        vin=car.vin,
        registration_number=car.registration_number,
        color=car.color,
        mileage=car.mileage,
        fuel_type=car.fuel_type,
        transmission=car.transmission
    )

    db.add(db_car)
    db.commit()
    db.refresh(db_car)

    return db_car


def update_car(db: Session, id: int, car: CarUpdate):
    db_car = db.get(Car, id)

    if db_car is None:
        return None

    for field, value in car.model_dump(exclude_unset=True, exclude={"updated_at"}).items():
        setattr(db_car, field, value)

    db.commit()
    db.refresh(db_car)

    return db_car


def delete_car(db: Session, id: int):
    db_car = db.get(Car, id)

    if db_car is None:
        return False

    db.delete(db_car)
    db.commit()

    return True