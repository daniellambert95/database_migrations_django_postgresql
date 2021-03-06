# Generated by Django 4.0.2 on 2022-02-02 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'address book',
                'verbose_name_plural': "Address's",
                'db_table': 'address_book',
            },
        ),
    ]
