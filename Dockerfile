FROM python:3.7

ENV PYTHONUNBUFFERED=1 PYTHONPATH=/opt/app/ DJANGO_SETTINGS_MODULE=hacker_news.settings

RUN DEBIAN_FRONTEND=noninteractive apt-get -y update \
    && apt-get -y install -y build-essential python3-dev \
    && pip install uwsgi \
    && true

COPY requirements/base.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /opt/app/
WORKDIR /opt/app/
RUN /opt/app/manage.py collectstatic --noinput
