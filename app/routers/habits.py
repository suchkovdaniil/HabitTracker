from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date
from typing import List

from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/habits", tags=["habits"])

@router.post("/", response_model=schemas.Habit)
def create_habit(habit: schemas.HabitCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Habit).filter_by(name=habit.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Habit already exists")
    db_habit = models.Habit(name=habit.name, description=habit.description)
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit

@router.get("/", response_model=list[schemas.Habit])
def list_habits(db: Session = Depends(get_db)):
    return db.query(models.Habit).all()

@router.post("/{habit_id}/log")
def log_habit(habit_id: int, log: schemas.LogCreate, db: Session = Depends(get_db)):
    habit = db.query(models.Habit).filter_by(id=habit_id).first()
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    existing_log = db.query(models.HabitLog).filter_by(habit_id=habit_id, date=log.date).first()
    if existing_log:
        raise HTTPException(status_code=400, detail="Already logged for this date")
    db_log = models.HabitLog(habit_id=habit_id, date=log.date)
    db.add(db_log)
    db.commit()
    return {"message": "Logged"}

@router.get("/{habit_id}/logs", response_model=List[schemas.Log])
def get_logs(habit_id: int, db: Session = Depends(get_db)):
    return db.query(models.HabitLog).filter_by(habit_id=habit_id).all()

@router.get("/{habit_id}/stats", response_model=schemas.Stats)
def get_stats(habit_id: int, db: Session = Depends(get_db)):
    total = db.query(models.HabitLog).filter_by(habit_id=habit_id).count()
    return {"total_completions": total}