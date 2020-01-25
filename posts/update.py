import requests
import logging
from typing import Mapping

from django.db import transaction
from lxml import html, etree

from posts.models import Post

logger = logging.getLogger(__name__)


PAGE_URL = 'https://news.ycombinator.com/'
MAX_POSTS_TO_FETCH = 30


# TODO: implement retry decorator in case of network error
def fetch_content() -> bytes:
    response = requests.get(PAGE_URL)
    response.raise_for_status()

    return response.content


def extract_posts(content: bytes) -> Mapping[int, Post]:
    posts = {}

    root = html.fromstring(content)
    post_items = root.xpath('//table[@class="itemlist"]//tr[@class="athing"]')
    for item in post_items[:MAX_POSTS_TO_FETCH]:
        try:
            post_id = int(item.attrib.get('id'))
            assert post_id

            storylinks = item.xpath('.//a[@class="storylink"]')
            assert len(storylinks) == 1

            url = storylinks[0].attrib.get('href')
            assert url

            title = storylinks[0].text.strip()
            assert title
        except Exception as e:
            logger.warning(f'Cant parse news item {e}: `{etree.tostring(item)}`')
            continue

        posts[post_id] = Post(id=post_id, title=title, url=url)

    return posts


def update_posts():
    content = fetch_content()
    new_posts = extract_posts(content)

    with transaction.atomic():
        existing_post_ids = (
            Post.objects.select_for_update().
            filter(pk__in=new_posts.keys()).
            values_list('pk', flat=True)
        )
        new_post_ids = set(new_posts.keys()).difference(existing_post_ids)
        if new_post_ids:
            Post.objects.bulk_create(new_posts[post_id] for post_id in new_post_ids)
            logger.info(f'Created new posts: {sorted(new_post_ids)}')
        else:
            logger.info(f'No new posts found')
