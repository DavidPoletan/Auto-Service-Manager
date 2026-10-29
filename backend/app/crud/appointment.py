from sqlalchemy.orm import Session
from backend.app.models.appointment import Appointment
from backend.app.schemas.appointment import AppointmentCreate, AppointmentUpdate

def get_appointment(db: Session, id: int):
    return db.get(Appointment, id)


def get_all_appointments(db: Session):
    return db.get(Appointment).all()


def create_appointment(db: Session, appointment: AppointmentCreate):
    db_appointment = Appointment(
        car_id=appointment.car_id,
        appointment_date=appointment.appointment_date,
        status=appointment.status,
        notes=appointment.notes,
    )

    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)

    return db_appointment


def update_appointment(db: Session, id: int, appointment: AppointmentUpdate):
    db_appointment = db.get(Appointment, id)

    if db_appointment is None:
        return None

    for field, value in appointment.model_dump(exclude_unset=True, exclude={"updated_at"}).items():
            setattr(db_appointment, field, value)
    
    db.commit()
    db.refresh(db_appointment)
    
    return db_appointment


def delete_appointment(db: Session, id: int):
    db_appointment = db.get(Appointment, id)

    if db_appointment is None:
        return False

    db.delete(db_appointment)
    db.commit()

    return True