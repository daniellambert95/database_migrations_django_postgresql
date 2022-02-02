# database_migrations_django_postgresql

This README is here to assist me when having to make Data Migrations
from a Django Postgres DB it is also a step-by-step guide.

- Create a venv
- Create a new Django Project
- Create and register a model in an app

# Creating postgresql database

$ createdb -h localhost \
-- createdb -h <db_name> \
$ psql -h localhost  \
-- psql -h <db_name>

=# DROP DATABASE IF EXISTS addressbook_django; \
=# CREATE DATABASE addressbook_django; \

=# CREATE USER username WITH PASSWORD 'password'; \
=#  ALTER ROLE username SET client_encoding TO ‘utf8’; \
=#  ALTER ROLE username SET default_transaction_isolation TO ‘read committed’; \
=#  ALTER DATABASE postgres SET timezone TO 'UTC'; \
=#  GRANT ALL PRIVILEGES ON DATABASE addressbook_django TO username; \
=#  \q \

- $ pip install django psycopg2

# Change DATABASES in settings.py and import local_settings.py / environment variables

DATABASES = { \
    'default': { \
        'ENGINE': 'django.db.backends.postgresql_psycopg2', \
        'NAME': 'addressbook_django', \
        'USER': 'daniel', \
        'PASSWORD': PASSWORD, \
        'HOST': 'localhost', \
        'POST': '', \
    } \
} \

- Edit ALLOWED HOSTS
just add '*'

- At the bottom of settings (Imports the password)
try:
    from local_settings import *
except ImportError:
    pass

# Create a model

class Address(models.Model):
    name = models.CharField(max_length=80, blank=False)
    email = models.EmailField(blank=False)
    address = models.CharField(max_length=200,  blank=False)

    class Meta:
        verbose_name = "address book"
        verbose_name_plural = "Address's"
        db_table = 'address_book'

    def __str__(self):
        return f"Here is the address for {self.name}"

# Register your model in admin.py

from django.contrib import admin
from .models import Address

1. admin.site.register(Address)

or

2. @admin.register(Address) \
class addressAdmin(admin.ModelAdmin): \
    list_display = ('id', 'name', 'email', 'address') \

# Make migrations and migrate

$ python manage.py makemigrations
$ python manage.py migrate

# Create superuser, runserver and add data to the model

$ python manage.py createsuperuser
$ python manage.py runderver
- http://127.0.0.1:8000/admin
