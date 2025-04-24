from pydantic import BaseModel
from datetime import date
from typing import List

class HabitBase(BaseModel):
    name: str
    description: str | None = None

class HabitCreate(HabitBase):
    pass

class Habit(HabitBase):
    id: int
    class Config:
        orm_mode = True

class LogCreate(BaseModel):
    date: date

class Log(BaseModel):
    id: int
    date: date
    class Config:
        orm_mode = True

class Stats(BaseModel):
    total_completions: int