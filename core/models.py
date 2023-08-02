from django.db import models

# Create your models here.
class Genre(models.Model):
    _id = models.CharField(max_length=255, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=255)

class Movie(models.Model):
    _id = models.CharField(max_length=255, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    number_in_stock = models.PositiveSmallIntegerField()
    daily_rental_rate = models.DecimalField(decimal_places=1, max_digits=2)  