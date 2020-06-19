from apscheduler.schedulers.blocking import BlockingScheduler
from collegescrapper import linkScrapper

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1)
def update_a():
    linkScrapper()


sched.start()
