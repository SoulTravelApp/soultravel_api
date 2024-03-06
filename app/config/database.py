from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://soultravelapp:mzryxB5jPmJ49TsS@soultravel-dev.oupucs5.mongodb.net/?retryWrites=true&w=majority&appName=soultravel-dev"
)


db = client.soultraveldev

user_score_collection = db["user_score"]
benefit_collection = db["benefit"]
user_benefit_collection = db["user_benefit"]
user_admin_collection = db["user_admin"]
