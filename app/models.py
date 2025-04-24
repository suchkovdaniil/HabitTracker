from sqlalchemy import Column, Integer, String, ForeignKey, Date, UniqueConstraint
from sqlalchemy.orm import relationship
from app.database import Base

class Habit(Base):
    __tablename__ = "habits"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)

    logs = relationship("HabitLog", back_populates="habit")

class HabitLog(Base):
    __tablename__ = "habit_logs"
    id = Column(Integer, primary_key=True, index=True)
    habit_id = Column(Integer, ForeignKey("habits.id"))
    date = Column(Date, nullable=False)

    habit = relationship("Habit", back_populates="logs")

    __table_args__ = (UniqueConstraint("habit_id", "date", name="_habit_date_uc"),)