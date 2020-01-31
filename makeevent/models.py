from django.db import models

# Create your models here.
'''
Attendee     
-Name
-ticket
      
Event
-location
-time & data 
-Attendee

ticket
-event 
-attendee 
-price
'''

class Attendee(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    attendees = models.ManyToManyField(Attendee, through='Ticket')

    def __str__(self):
        return self.name

class Ticket(models.Model):
    price = models.DecimalField(decimal_place=2, max_digits=3)
    event = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f'Attendee {self.attendee} at Event {self.event}'