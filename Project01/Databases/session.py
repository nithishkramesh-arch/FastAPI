from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlmodel import SQLModel, Session
from sqlalchemy.orm import sessionmaker
# from .models import ShipmentModel
from config import settings


engine = create_async_engine(
  url=settings.POSTGRES_DATABASE,
  echo=True, #to get the executed statements
  # connect_args={
  #   "check_same_thread":False #avoid running the db and the fastapi in the same thread, for postgres, its not required
  # }
)

async def createDBTables():
  async with engine.begin() as connection:
    await connection.run_sync(
    SQLModel.metadata.create_all )


async def getSession():
  asyncSession = sessionmaker(bind=engine, class_= AsyncSession, expire_on_commit=False )

  async with asyncSession() as session:
    yield session
#session.get(ShipmentModel, 1)
#session.add(ShipmentModel(item="nithish", status="delivered"))

#session.commit()

SessionDep = Annotated[AsyncSession, Depends(getSession)]