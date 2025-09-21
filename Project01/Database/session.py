from sqlalchemy import create_engine
from sqlmodel import SQLModel
engine = create_engine(
  url="sqlite:///sqlite.db",
  echo=True, #to get the executed statements
  connect_args={
    "check_same_thread":False #avoid running the db and the fastapi in the same thread, for postgres, its not required
  }
)

SQLModel.metadata.create_all(bind = engine)
