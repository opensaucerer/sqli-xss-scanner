from flask import current_app
from pymongo import MongoClient
import requests
import random
import os
from dotenv import load_dotenv
load_dotenv()
MONGO_URI = os.environ.get('MONGO_URI')

client = MongoClient(MONGO_URI)
db = client.pentest

# mongo = PyMongo(uri=MONGO_URI)


# function for worker test
def count_words_at_url(url):

    print('STARTING THE TASK')
    resp = requests.get(url)
    l = len(resp.text.split())
    num = random.randint(0, l)

    # with open('len.txt', 'a') as f:
    #     f.write(str(l) + '\n')
    #     f.close()
    # with current_app._get_current_object().app_context():
    db.workers.insert_one({'random': num})

    print('STARTING THE TASK END')
    return l


# count_words_at_url('https://google.com')
