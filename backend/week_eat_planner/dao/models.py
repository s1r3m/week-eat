from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from week_eat_planner.dao.database import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str]


class Meal(Base):
    __tablename__ = 'meals'

    id: Mapped[int] = mapped_column(primary_key=True)


class Week(Base):
    __tablename__ = 'weeks'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('weeks.id'), nullable=True)
    week_start: Mapped[str]
    meals: Mapped[list[Meal]] = relationship(Meal, backref='week')
