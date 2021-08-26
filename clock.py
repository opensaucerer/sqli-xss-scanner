from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from rq import Queue
from worker import conn
from t import count_words_at_url
from pytz import utc
import os
MONGO_URI = os.environ.get('MONGO_URI')
from uuid import uuid4
# creating the task queue connection
q = Queue(connection=conn)

from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


jobstores = {
    'mongo': MongoDBJobStore(),
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

sched = BlockingScheduler(
    jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)


@sched.scheduled_job('interval', seconds=7)
def timed_job():
    q.enqueue(count_words_at_url, 'http://heroku.com')
    print('This job is run every three minutes.')


class Scheduler:

    latency = {
        'daily': 'mon-fri',
        'weekly': 'mon',
        'monthly': ''
    }

    def test(self):
        print('THIS JOB IS A TEST JOB')

    def schedule(self, form):
        lat = form['latency']
        h = int(form['time'].split(':')[0])
        m = int(form['time'].split(':')[1])
        return sched.add_job(self.test, trigger='cron', id=uuid4(), day_of_week=self.latency[lat], hour=h, minute=m)


# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=11, minute=8)
# def scheduled_job():
#     result = q.enqueue(count_words_at_url, 'http://heroku.com')
#     print('This job is run every weekday at 5pm.')
# sched.add_job(lambda: sched.print_jobs(), 'interval', seconds=5)
sched.start()
