from django.db import models

# Create your models here.
class FlightSearch(models.Model):
    origin = models.CharField( max_length=50)
    destination = models.CharField(max_length=50)
    departure_date = models.DateField()
    return_date = models.DateField()
    passenger_count = models.IntegerField()
