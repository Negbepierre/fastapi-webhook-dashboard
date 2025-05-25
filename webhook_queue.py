import redis
from rq import Queue

r = redis.Redis(host="localhost", port=6379, db=0)
q = Queue("webhooks", connection=r)
