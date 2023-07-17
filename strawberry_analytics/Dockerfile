FROM fedora:latest

WORKDIR /usr/src/app

COPY . .

RUN dnf update -y --refresh && \
    dnf install -y python python-pip && \
    pip install gunicorn django requests python-multipart SQLAlchemy PyMySQL

CMD gunicorn strawberry_analytics.wsgi:application --bind 0.0.0.0:14567
