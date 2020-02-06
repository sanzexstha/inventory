from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='t1!9hu0bx5c#wdfe@hqfsbxredlsk0fb3%$xee*_lq%$4)v4m0')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
