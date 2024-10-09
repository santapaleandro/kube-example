from fastapi import FastAPI
from pymongo import MongoClient
import os

app = FastAPI()

# Connect to MongoDB
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = MongoClient(MONGO_URL)
db = client["test_db"]

@app.get("/")
async def root():
    return {"message": "Hello World from python FastAPI app !!!"}

@app.post("/add")
async def add_data(item: dict):
    db.test_collection.insert_one(item)
    return {"status": "Item added", "item": item}

@app.get("/items")
async def get_items():
    items = list(db.test_collection.find({}, {"_id": 0}))
    return {"items": items}