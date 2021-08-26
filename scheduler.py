from dotenv import load_dotenv
load_dotenv()
import datetime
import os
import pymongo

client = pymongo.MongoClient(os.environ.get('MONGO_URI'))
db = client.pentest


def save_data_to_mongo(data):
    response = db.test.insert_one(data)


if __name__ == "__main__":
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {}
    data["text"] = "Hello World"
    data["date_time"] = date_time
    save_data_to_mongo(data)
