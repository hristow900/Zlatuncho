from apscheduler.schedulers.background import BackgroundScheduler
from collector import run_collector
import os

scheduler = BackgroundScheduler()


def start_scheduler():
    if os.getenv("COLLECTOR_SCHEDULE_ENABLED", "false").lower() == "true":
        hour = int(os.getenv("COLLECTOR_HOUR", 9))
        minute = int(os.getenv("COLLECTOR_MINUTE", 0))

        scheduler.add_job(run_collector, "cron", hour=hour, minute=minute)
        scheduler.start()
