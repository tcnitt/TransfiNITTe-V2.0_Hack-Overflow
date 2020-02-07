from django.db import models
from django.utils import timezone

# Create your models here.
class Vehicle(models.Model):
    car_no=   models.CharField(max_length=200)
    entry_time= models.DateTimeField(default=timezone.now)
    exit_time=  models.DateTimeField(default=timezone.now)
    car_model=   models.CharField(max_length=200)
    def __str__(self):
        return self.car_no

