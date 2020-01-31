from django.db import models

# Create your models here.

class Driver(models.Model):
    name = models.CharField(max_length=50)
    rating = models.DecimalField(decimal_place=2, max_digits=3)

    def __str__(self):
        return self.name

class Passenger(models.Model):
    name = models.CharField(max_length=50)
    rating = models.DecimalField(decimal_place=2, max_digits=3)
    drivers = models.ManyToManyField(Driver, through='Trip')

    def __str__(self):
        return self.name

class Trip(models.Model):
    start_location = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    driver = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return f'From {self.start_location} to {self.destination}'

