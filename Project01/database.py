import sqlite3
from contextlib import contextmanager
#from .main import Item
#finalResult :list[Item] = []



class DataBase:

  # def __init__(self):
  #   self.connection = sqlite3.connect("Sqlite.db")
  #   self.cursor = self.connection.cursor()

#if we are using context manager (sample syntax below), then using this will invoke first, like init

#sample syntax
#context manager -> with open("some") as f -- likewise we are going to create context manager for this database file
  def __enter__(self):
    self.createConnection()
    self.createTable()
    return self

  def createConnection(self):
    self.connection = sqlite3.connect("Sqlite.db")
    self.cursor = self.connection.cursor()


  def createTable(self):
     self.cursor.execute("""
      create table if not exists shipment (
               id int, 
               item text, 
               status text)
""")
     self.saveRecord()

  def createTable2(self):
     self.cursor.execute("""
      create table if not exists students (
               id int, 
               name text, 
               age int)
""")
     self.saveRecord()

  def insertRecord(self, itemId, itemName, itemStatus):
    self.cursor.execute("""
        insert into shipment values(:id, :itemName, :itemStatus)
               """, {
                 "id":itemId,
                 "itemName":itemName,
                 "itemStatus":itemStatus
               })
    self.saveRecord()

  def insertRecord2(self, itemId, name, age):
    self.cursor.execute("""
        insert into students values(:id, :itemName, :itemStatus)
               """, {
                 "id":itemId,
                 "itemName":name,
                 "itemStatus":age
               })
    self.saveRecord()

  def getRecord(self, itemId):
    self.cursor.execute("select * from shipment where id=:id", {
      "id":itemId
    })
    result = self.cursor.fetchmany(1)
    return result

  def dropTable(self):
    self.cursor.execute("drop table shipment")
    self.cursor.execute("drop table shipmentmodel")
     
  def saveRecord(self):
    self.connection.commit()

  def close(self):
    self.cursor.close()
    self.connection.close()

#once context manager completes it needs to exit, we use this
  def __exit__(self, *args):
    self.close()

#either we can use the above method (__enter__ and __exit__ or the below manageDB), our context manager will take care of it..

#@contextmanager
# def manageDb():
#   db = DataBase()
#   #db.createConnection()
  
#   #db.createTable()
#   #db.getRecord(1)
#   yield db

#   db.close()

with DataBase() as db:
  #print(db.getRecord(1))
  #db.dropTable()
  #db.insertRecord("book", "delivered")
  #db.insertRecord(4,"laptop", "in transit")
  #db.insertRecord(3,"hen", "packaging")
  # db.createTable2()
  # db.insertRecord2(1, "nithish", 25)
  # db.insertRecord2(2, "harini", 24)
  pass




 # cursor.execute("select * from shipment")




# result = cursor.fetchall()
# result2 = cursor.fetchmany(2) #how many records to fetch.
# result3 = cursor.fetchone() #fetch one record

# print(result)

# print(finalResult)


# #inorder to avoid sql injection, we need to use this functionality
# value1 = "delivered"
# value2 = 2
# cursor.execute("""update shipment set status = ?
#                where id = ?
#                """,(value1, value2))

# cursor.execute("""update shipment set status = :key1
#                where id = :key2
#                """,{
#                  "key1":value1,
#                  "key2":value2
#                })
# #we need to avoid the following functionality
# # cursor.execute(f"""update shipment set status = {value1}
# #                where id = {value2}
# #                """)
# connection.commit() 

# connection.close()

# import json

# print("logic comes here")
# items= []

# with open("shipments.json") as file:
#   data = json.load(file)
#   for value in data:
#     items.append(value)


# def save():
#   with open("shipments.json", "w") as file:
#     json.dump(items, file)

