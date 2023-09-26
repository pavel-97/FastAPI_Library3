import smtplib, ssl

from celery import Celery

from .conf import RABBITMQ_LOGIN, RABBITMQ_PASSWORD, EMAIL, EMAIL_PASSWORD


app = Celery('tasks', broker=f'amqp://{RABBITMQ_LOGIN}:{RABBITMQ_PASSWORD}@rabbitmq', backend='redis://redis')


@app.task
def add(x: int, y: int) -> int:
    return x + y


@app.task
def send_mail():
    port = 465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', port=port, context=context) as server:
        server.login(EMAIL, EMAIL_PASSWORD)
        server.sendmail(EMAIL, 'gill1488@mail.ru', msg='Hello, World')
    