from dotenv import load_dotenv
load_dotenv()
import datetime
import os
import pymongo
import requests

client = pymongo.MongoClient(os.environ.get('MONGO_URI'))
db = client.pentest


def get_all_scan():
    response = db.schedule.find()

    return response


def check(data):
    time = datetime.datetime.now().time().hour
    if data['freq'] == 'twice':
        if time >= 0 and time < 9:
            res = requests.get(
                f'https://pen-tester.herokuapp.com/w_report?id={data["owner"]}&url={data["url"]}&email={data["email"]}')

        elif time >= 12 and time < 13:
            res = requests.get(
                f'https://pen-tester.herokuapp.com/w_report?id={data["owner"]}&url={data["url"]}&email={data["email"]}')

    else:
        if time >= 12 and time < 13:
            res = requests.get(
                f'https://pen-tester.herokuapp.com/w_report?id={data["owner"]}&url={data["url"]}&email={data["email"]}')


def scan_d(data):
    check(data)
    return True


def scan_w(data):
    day = datetime.datetime.now().date().weekday()
    if day == 5:
        check(data)
    return True


if __name__ == "__main__":
    scans = get_all_scan()
    for scan in scans:
        if scan['latency'] == 'daily':
            scan_d(scan)
        else:
            scan_w(scan)
