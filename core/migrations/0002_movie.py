# Generated by Django 4.2.4 on 2023-08-02 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('_id', models.CharField(editable=False, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('number_in_stock', models.PositiveSmallIntegerField()),
                ('daily_rental_rate', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
    ]
