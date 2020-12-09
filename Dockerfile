FROM python:3.6.11-stretch

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y libpq-dev gcc

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


RUN mkdir /app
COPY . /app
WORKDIR /app

RUN mkdir -p /vol/web/
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser --no-create-home --disabled-login user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

CMD ["entrypoint.sh"]