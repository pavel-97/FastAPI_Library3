import smtplib, ssl

from celery import Celery

from pydantic import EmailStr

from .conf import RABBITMQ_LOGIN, RABBITMQ_PASSWORD, EMAIL, EMAIL_PASSWORD


app = Celery('tasks', broker=f'amqp://{RABBITMQ_LOGIN}:{RABBITMQ_PASSWORD}@rabbitmq', backend='redis://redis')


@app.task
def send_mail(mail: EmailStr):
    port = 465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', port=port, context=context) as server:
        server.login(EMAIL, EMAIL_PASSWORD)
        server.sendmail(EMAIL, mail, msg=f'You are login')
    return True