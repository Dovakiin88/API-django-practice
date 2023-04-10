from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self): #NOTE: this help makes things readable
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField(max_length=4)
    number_in_stock = models.IntegerField(max_length=3)
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now)

#NOTE: to register this info, use py manage.py makemigrations
#NOTE: to migrate everything run py manage.py migrate
#NOTE: DO NOT EVER EVER EVER EVER EVER EVER EVER DELETE Migrations


