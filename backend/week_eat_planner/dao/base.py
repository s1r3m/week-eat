from typing import Generic, TypeVar

from loguru import logger
from pydantic import BaseModel
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from week_eat_planner.dao.database import Base


T = TypeVar('T', bound=Base)


class BaseDAO(Generic[T]):
    model: type[T]

    @classmethod
    async def get_one_or_none_by_id(cls, session: AsyncSession, obj_id: int) -> T | None:
        logger.info(f'Getting {cls.model.__name__} by id={obj_id}')
        try:
            query = select(cls.model).filter(cls.model.id == obj_id)
            result = await session.execute(query)
            record = result.scalar_one_or_none()
            if record:
                logger.info(f'{cls.model.__name__} with id={obj_id} has been successfully found')
            else:
                logger.warning(f'{cls.model.__name__} with id={obj_id} not found')
        except SQLAlchemyError as exc:
            logger.exception(f'Error while getting {cls.model.__name__} by id={obj_id}: {exc}')
            raise exc

        return record

    @classmethod
    async def get_one_or_none(cls, session: AsyncSession, _filter: BaseModel) -> T | None:
        model_dict = _filter.model_dump(exclude_unset=True)
        logger.info(f'Getting {cls.model.__name__} by filter={model_dict}')
        try:
            query = select(cls.model).filter_by(**model_dict)
            result = await session.execute(query)
            record = result.scalar_one_or_none()
            if record:
                logger.info(f'{cls.model.__name__} with filter={model_dict} has been successfully found')
            else:
                logger.warning(f'{cls.model.__name__} with filter={model_dict} not found')
        except SQLAlchemyError as exc:
            logger.exception(f'Error while getting {cls.model.__name__} by filter={model_dict}: {exc}')
            raise exc

        return record

    @classmethod
    async def add(cls, session: AsyncSession, model: BaseModel) -> T:
        model_dict = model.model_dump(exclude_unset=True)
        logger.info(f'Adding {cls.model.__name__} with data={model_dict}')
        instance = cls.model(**model_dict)
        try:
            session.add(instance)
            await session.flush()
            logger.info(f'{cls.model.__name__} has been successfully added')
        except SQLAlchemyError as exc:
            await session.rollback()
            logger.exception(f'Error while adding {cls.model.__name__}: {exc}')
            raise exc

        return instance
