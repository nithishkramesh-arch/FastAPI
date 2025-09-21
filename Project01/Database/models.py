from sqlmodel import SQLModel, Field, Table


#we can add customName in class name, since we can specify the table in the __tablename__ property 
class ShipmentModel(SQLModel, Table=True):
  __tablename__ = "Shipment"

  id:int = Field(primary_key=True) 
  item:str
  status:str