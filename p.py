
from rq import Queue
from worker import conn
from t import *

q = Queue(connection=conn)


q.enqueue(count_words_at_url, 'http://heroku.com')
