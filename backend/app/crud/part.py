from sqlalchemy.orm import Session
from backend.app.models.part import Part
from backend.app.schemas.part import PartCreate, PartResponse, PartUpdate

def get_part(db: Session, id: int):
    return db.get(Part, id)


def get_all_parts(db: Session):
    return db.query(Part).all()


def create_part(db: Session, part: PartCreate):
    db_part = Part(
        name=part.name,
        manufacturer=part.manufacturer,
        part_number=part.part_number,
        unit_price=part.unit_price,
        quantity_in_stock=part.quantity_in_stock,
        minimum_stock=part.minimum_stock
    )

    db.add(db_part)
    db.commit()
    db.refresh(db_part)

    return db_part


def update_part(db: Session, part_id: int, part: PartUpdate):
    db_part = db.get(Part, part_id)

    if db_part is None:
        return None

    for field, value in part.model_dump(exclude_unset=True, exclude={"updated_at"}).items():
        setattr(db_part, field, value)

    db.commit()
    db.refresh(db_part)

    return db_part


def delete_part(db: Session, part_id: int):
    db_part = db.get(Part, part_id)

    if db_part is None:
        return False

    db.delete(db_part)
    db.commit()

    return True