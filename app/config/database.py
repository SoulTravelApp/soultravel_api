from pymongo import MongoClient

client = MongoClient("mongodb+srv://soultravelapp:mzryxB5jPmJ49TsS@soultravel-dev.oupucs5.mongodb.net/?retryWrites=true&w=majority&appName=soultravel-dev")


db = client.soultraveldev

user_score_collection = db["user_score"]
