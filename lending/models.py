from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Object(models.Model):
    ownedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

class Contract(models.Model):
    lateFee = models.IntegerField()
    rentalPrice = models.IntegerField()
    startTime = models.DateField()
    endTime = models.DateField()
    timeReturned = models.DateField()
    borrowedObject = models.ForeignKey(Object, on_delete=models.CASCADE)
    borrowedBy = models.ForeignKey(User, on_delete=models.CASCADE)
