from pymongo import MongoClient

client = MongoClient("mongodb+srv://soultravelapp:mzryxB5jPmJ49TsS@soultravel-dev.oupucs5.mongodb.net/?retryWrites=true&w=majority&appName=soultravel-dev")


db = client.todo_app

collection_name = db["todos_app"]
