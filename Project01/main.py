from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from typing import  Any
from pydantic import BaseModel, Field
from contextlib import asynccontextmanager
from rich import print, panel
#from sqlmodel import Session #customize the print message
from Project01.Databases.models import  ShipmentGetModel, ShipmentModel, ShipmentUpdateModel, Students
from Project01.Databases.session import SessionDep, createDBTables

#whatever we mentioned here, we can inject while fastapi starts
#callable function with context manager.
@asynccontextmanager
async def lifeSpan(app:FastAPI):
  print(panel.Panel("Server is started", border_style="green"))
  #this is to create tables while server started running.
  createDBTables()
  yield 
  print(panel.Panel("server is shutdown", border_style="red"))

app = FastAPI(lifespan=lifeSpan)

#either we can use like this or we can create this in session file and directly import the session type. 
#Added the code in the session class
#sessionDep = Annotated[Session, Depends(getSession)]

items: list[dict] = [
  {
    "id":1, 
    "item":"book",
    "status":"in transit"
  },
  {
    "id":2, 
    "item":"wall",
    "status":"delivered"
  },
  {
    "id":3, 
    "item":"car",
    "status":"packaging"
  }
  ,
  {
    "id":4, 
    "item":"bin",
    "status":"in transit"
  }
]

@app.get("/Schedule")
def getSchedule():
  return {
    "id":1,
    "item":"Container",
    "contains":"ball"
  }

@app.get("/Shipment/{id}", status_code=status.HTTP_200_OK)
def getShipmentById(id:int, session : SessionDep) -> dict | Any:
  result = session.get(ShipmentModel, id)
  if(not result):
    raise HTTPException(status_code=404, detail={"message":"there is no record like that"})
  return result
  # for item in items:
  #   if(item["id"] == id):
  #     return item
  # return HTTPException(status_code=404, detail="you are a fool")






@app.post("/Shipment/NewShipment")
def addShipment(newItem:ShipmentGetModel, session:SessionDep):
  # shipmentDetails = ShipmentModel(
  #   **item.model_dump()
  # )
  #either above one or below one
  shipmentDetails = ShipmentModel(
    item=newItem.item,
    status=newItem.status
  )
  session.add(shipmentDetails)
  session.commit()
  session.refresh(shipmentDetails)
  return shipmentDetails.model_dump()

@app.put("/Shipment/Update/")
async def updateShipment(id:int, currentData:ShipmentUpdateModel, session:SessionDep):
  existingData = session.get(ShipmentModel, id)
  if(not existingData):
    existingData.sqlmodel_update(currentData.model_dump(exclude_unset=False)) #Need to work on this, 
    session.add(existingData)
    session.commit()
    session.refresh(existingData)
  else:
    raise HTTPException(status_code=404, detail="No data")

  # existingData.item = currentData.item
  # existingData.status = currentData.status

  return existingData

@app.delete("/Shipment")
async def deleteShipment(itemId:str, session:SessionDep):
  result = session.get(ShipmentModel, id)
  session.delete(session.get(ShipmentModel, id))
  session.commit()
  return result.id



#This below api is to use some other api documentation.
#For eg, scalar. it is one of the API documentation
@app.get("/scalar", include_in_schema=False)
def getScalarApiReference():
  return get_scalar_api_reference(openapi_url=app.openapi_url, title="Scalar API")



