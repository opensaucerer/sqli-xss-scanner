from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler


from rq import Queue
from worker import conn
from t import count_words_at_url
q = Queue(connection=conn)

# sched = BackgroundScheduler(daemon=True)

sched = BlockingScheduler(daemon=True)


@sched.scheduled_job('interval', seconds=7)
def timed_job():
    q.enqueue(count_words_at_url, 'http://heroku.com')
    print('This job is run every three minutes.')


# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=11, minute=8)
# def scheduled_job():
#     result = q.enqueue(count_words_at_url, 'http://heroku.com')
#     print('This job is run every weekday at 5pm.')


sched.start()

# sched.add_job(lambda: sched.print_jobs(), 'interval', seconds=5)

# sched.start()
