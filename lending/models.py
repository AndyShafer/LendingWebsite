from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, editable=False)
    address = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    bio = models.CharField(max_length=500, default='')


class Object(models.Model):
    ownedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

class Contract(models.Model):
    lateFee = models.IntegerField(default=0)
    rentalPrice = models.IntegerField(default=0)
    startTime = models.DateField(blank=True, null=True)
    endTime = models.DateField(blank=True, null=True)
    timeBorrowed = models.DateField(blank=True, null=True)
    timeReturned = models.DateField(blank=True, null=True)
    borrowedObject = models.ForeignKey(Object, on_delete=models.CASCADE)
    borrowedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    acceptedByOwner = models.BooleanField(default=False)

