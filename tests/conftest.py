import pytest
from decouple import config
from maistodos import settings


URL = 'http://' + str(config('HOST')) + ":" + str(config('DJANGO_PORT'))


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE':   config('ENGINE'),
        'NAME':     config('MYSQL_TEST_DATABASE_NAME'),
        'USER':     config('MYSQL_TEST_USER'),
        'PASSWORD': config('MYSQL_TEST_PASSWORD'),
        'HOST':     config('HOST'),
        'PORT':     config('DATABASE_TEST_PORT'),
    }