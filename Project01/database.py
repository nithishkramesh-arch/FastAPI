import sqlite3
from .main import Item
finalResult :list[Item] = []



class DataBase:


  def __init__(self):
    self.connection = sqlite3.connect("Sqlite.db")
    self.cursor = self.connection.cursor()
    self.cursor.execute("""
      create table if not exists shipment (
               id int, 
               item text, 
               status text)
""")



  

# cursor.execute("""
#   insert into shipment values(1, "book", "delivered")
#                """)

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


