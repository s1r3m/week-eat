from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from week_eat_planner.dao.database import Base


# Association table for the many-to-many relationship between Meal and Week
meal_week_association = Table(
    'meal_week_association',
    Base.metadata,
    Column('meal_id', ForeignKey('meals.id'), primary_key=True),
    Column('week_id', ForeignKey('weeks.id'), primary_key=True),
)


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str]


class Meal(Base):
    __tablename__ = 'meals'

    id: Mapped[int] = mapped_column(primary_key=True)
    weeks: Mapped[list['Week']] = relationship('Week', secondary=meal_week_association, back_populates='meals')


class Week(Base):
    __tablename__ = 'weeks'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True)
    week_start: Mapped[str]
    meals: Mapped[list[Meal]] = relationship('Meal', secondary=meal_week_association, back_populates='weeks')
