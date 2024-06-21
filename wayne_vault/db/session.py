import asyncio
import logging
from typing import AsyncGenerator, Optional

from sentry_sdk import capture_exception
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker

from wayne_vault.core.config import settings

async_session: Optional[AsyncEngine] = None
engine: Optional[AsyncEngine] = None


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    try:
        session = async_session()
        logging.debug("Returned database session %d for task %s", id(session), asyncio.current_task().get_name())
        yield session

    except Exception as e:
        logging.error("Rolling back session %d because of %s", id(session), e)
        capture_exception(e)
        await rollback_session(session)

    finally:
        await finalize_session(session)


def initialize_database():
    global async_session, engine

    engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI,
                                 echo=True,
                                 pool_size=settings.DB_POOL_SIZE,
                                 pool_pre_ping=settings.DB_POOL_PRE_PING,
                                 pool_recycle=settings.DB_POOL_RECYCLE)
    async_session = sessionmaker(engine, expire_on_commit=False, autocommit=False, autoflush=False, class_=AsyncSession)


async def finalize_session(session: AsyncSession):
    try:
        logging.info("Committing session %d", id(session))
        await session.commit()

    except Exception as e:
        logging.error("Error while committing session: %s", e)
        capture_exception(e)
        await session.rollback()
        raise

    finally:
        logging.debug("Closing session %d", id(session))
        await session.close()


async def rollback_session(session: AsyncSession):
    await session.rollback()
    await session.close()
