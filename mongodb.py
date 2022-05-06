
import pymongo
import json
import logging as lg
#!pip install dnspython

def load_mongodb(df,collection):
  client = pymongo.MongoClient("mongodb+srv://Test:test@cluster0.ucbeu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
  db = client.test_db
  collection1= db[collection]

  df.reset_index(inplace=True)
  house_dict=df.to_dict("records")
  collection1.insert_many(house_dict)


def all_data(coll1):
  client = pymongo.MongoClient("mongodb+srv://Test:test@cluster0.ucbeu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
  db = client.test_db
  collection1= db[coll1]
  data = collection1.find()
  return[i for i in data]
def retrive_data(coll1,x):
  client = pymongo.MongoClient("mongodb+srv://Test:test@cluster0.ucbeu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
  db = client.collection1
  collection1= db[coll1]
  data = collection1.find(x)
  result1= [i["Addreses"] for i in data]
  return result1





