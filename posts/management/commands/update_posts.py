from django.core.management import BaseCommand

from posts.update import update_posts


class Command(BaseCommand):
    def handle(self, *args, **options):
        update_posts()
