from t.proj.settings import *

CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_RESULT_BACKEND = "django_celery_results.backends.database.DatabaseBackend"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'postgres',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'devpass',
        'OPTIONS': {
            'connect_timeout': 1000,
        }
    },
}
