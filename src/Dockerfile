FROM python:3.8-buster

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    useradd -ms /bin/bash app

COPY --chown=app:app app.py gunicorn.conf.py requirements.txt /home/app/
COPY --chown=app:app resources/ /home/app/resources/

RUN pip install -r /home/app/requirements.txt

EXPOSE 8000

USER app

WORKDIR /home/app

ENTRYPOINT [ "gunicorn" ]

CMD [ "app:app" ]
