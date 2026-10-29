from sqlalchemy.orm import Session
from backend.app.models.workorder import WorkOrder
from backend.app.schemas.workorder import WorkOrderCreate, WorkOrderUpdate

def get_workorder(db: Session, id: int):
    return db.get(WorkOrder, id)


def get_all_workorders(db: Session):
    return db.query(WorkOrder).all()


def create_workorder(db: Session, workorder: WorkOrderCreate):
    db_workorder = WorkOrder(
        appointment_id=workorder.appointment_id,
        mechanic_id=workorder.mechanic_id,
        problem_description=workorder.problem_description,
        labor_cost=workorder.labor_cost,
        status=workorder.status,
        odometer=workorder.odometer,
        diagnosis=workorder.diagnosis,
        work_performed=workorder.work_performed,
        recommendations=workorder.recommendations
    )

    db.add(db_workorder)
    db.commit()
    db.refresh(db_workorder)

    return db_workorder


def update_workorder(db: Session, id: int, workorder: WorkOrderUpdate):
    db_workorder = db.get(WorkOrder, id)

    if db_workorder is None:
        return None

    for field, value in workorder.model_dump(exclude_unset=True, exclude={"updated_at"}).items():
            setattr(db_workorder, field, value)
    
    db.commit()
    db.refresh(db_workorder)
    
    return db_workorder


def delete_workorder(db: Session, id: int):
     db_workorder = db.get(WorkOrder, id)

     if db_workorder is None:
          return False

     db.delete(db_workorder)
     db.commit()

     return True