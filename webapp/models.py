from django.db import models

class ParkingSpot(models.Model):
    ParkingSpotID = models.IntegerField(default=0)
    UserAssinged = models.CharField(max_length=10)

class User(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Password = models.CharField(max_length=20, default='')
