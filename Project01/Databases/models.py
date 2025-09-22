from pydantic import BaseModel
from sqlmodel import SQLModel, Field


#we can add customName in class name, since we can specify the table in the __tablename__ property 
class ShipmentModel(SQLModel, table=True):
  #__tablename__ = "Shipment"
  __tablename__ = "Shipment"

  id:int|None = Field(default=None,primary_key=True) 
  item:str
  status:str

class Shipment(BaseModel):
  item:str
  status:str

class Students(SQLModel, table = True):
  __tablename__ = "students"
  id:int|None = Field(default=None,primary_key=True) 
  name:str
  age:int
  pass

class ShipmentGetModel(BaseModel):
  item:str
  status:str

class ShipmentUpdateModel(BaseModel):
  #id:int
  item:str | None =Field(default=None)
  status:str | None = Field(default = None)
