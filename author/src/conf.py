from typing import Final

from environs import Env


env = Env()
env.read_env()


RABBITMQ_LOGIN: Final = env.str('RABBITMQ_DEFAULT_USER')
RABBITMQ_PASSWORD: Final = env.str('RABBITMQ_DEFAULT_PASS')

EMAIL: Final = env.str('EMAIL')
EMAIL_PASSWORD: Final = env.str('EMAIL_PASSWORD')