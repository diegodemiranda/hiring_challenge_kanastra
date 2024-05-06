from sqlalchemy.orm import Session
from backend import models
from backend import schemas


def get_charge(db: Session, charge_id: int):
    return db.query(models.Charge).filter(models.Charge.id == charge_id).first()


def get_charges(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Charge).offset(skip).limit(limit).all()


def create_charge(db: Session, charge: schemas.ChargeCreate):
    db_charge = models.Charge(
        name=charge.name,
        government_id=charge.governmentId,
        email=charge.email,
        debt_amount=charge.debtAmount,
        debt_due_date=charge.debtDueDate
    )
    db.add(db_charge)
    db.commit()
    db.refresh(db_charge)
    return db_charge


def update_charge(db: Session, charge_id: int, charge_data: schemas.ChargeCreate):
    db_charge = db.query(models.Charge).filter(models.Charge.id == charge_id).first()
    if db_charge:
        for key, value in charge_data.dict().items():
            setattr(db_charge, key, value)
        db.commit()
        db.refresh(db_charge)
    return db_charge


def delete_charge(db: Session, charge_id: int):
    db_charge = db.query(models.Charge).filter(models.Charge.id == charge_id).first()
    if db_charge:
        db.delete(db_charge)
        db.commit()
    return db_charge
