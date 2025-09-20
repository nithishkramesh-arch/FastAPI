from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from typing import Any
from pydantic import BaseModel
#from .database import items, save
app = FastAPI()

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
def getShipmentById(id:int) -> dict | Any:
  for item in items:
    if(item["id"] == id):
      return item
  return HTTPException(status_code=404, detail="you are a fool")



class Item(BaseModel):
  item:str
  status:str



@app.post("/Shipment/NewShipment")
def addShipment(item:Item):
  newItem = {
    "id": items[len(items) - 1]["id"] + 1,
    "item":item.item,
    "status":item.status
  }
  items.append(newItem)
  return items

@app.put("/Shipment", response_model=list[dict] | Any)
async def updateShipment(updateItem:Item):
  # for item in items:
  #   if(item["item"] == updateItem.itemName):
  #     item["item"] = updateItem.itemName
  #     item["status"] = updateItem.status
  #     break
  existingItem = {}
  for item in items:
    if(item["item"] == updateItem.item):
      existingItem = item
      break

  if(existingItem == {}):
    raise HTTPException(status_code=404, detail="there is no item")
  existingItem.update(updateItem)
 # save()
  return items

@app.delete("/Shipment")
async def deleteShipment(itemName:str):
  for index, item in enumerate(items):
    if(item["item"] == itemName):
      items.pop(index)
      break
  return items



#This below api is to use some other api documentation.
#For eg, scalar. it is one of the API documentation
@app.get("/scalar", include_in_schema=False)
def getScalarApiReference():
  return get_scalar_api_reference(openapi_url=app.openapi_url, title="Scalar API")



