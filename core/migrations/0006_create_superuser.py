# Generated by Django 4.2.4 on 2023-08-23 23:48

from django.db import migrations
from django.contrib.auth.models import User


def create_admin_user(apps, schema_editor):
    User.objects.create_superuser(username='realdami', password='realpassword')


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_genre__id'),
    ]

    operations = [migrations.RunPython(create_admin_user)]
