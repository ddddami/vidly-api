from django.db import models

# Create your models here.
class Genre(models.Model):
    _id = models.CharField(max_length=255, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=255)