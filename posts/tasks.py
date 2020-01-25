from hacker_news.celery import app as celery_app
from .update import update_posts


@celery_app.task(ignore_result=True)
def update_posts_task():
    update_posts()
