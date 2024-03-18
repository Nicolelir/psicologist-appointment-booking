from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from services.models import Services

# Create your models here.
SERVICES_TYPES= (("online individual therapy", "Online Individual Therapy"), 
                 ("online family therapy", "Online Family Therapy"), 
                 ("workshop", "Workshop"))


# generate hourly time slots from 8 am to 6 pm
TIME_CHOICES = []
start_time = datetime.strptime("09:00", "%H:%M")
end_time = datetime.strptime("18:00", "%H:%M")

while start_time < end_time:
    time_slot = start_time.strftime(
        "%H:%M") + " - " + (start_time + timedelta(hours=1)).strftime("%H:%M")
    TIME_CHOICES.append((time_slot, time_slot))
    start_time += timedelta(hours=1)

class Booking(models.Model):
    """ A model for booking an appointment """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    service = models.CharField(max_length=50, choices=SERVICES_TYPES, default="online_individual_therapy")
    date = models.DateField(default=datetime.now, blank=True)
    time = models.CharField(max_length=20, choices=TIME_CHOICES, default="09:00 - 10:00")
    notes = models.TextField(blank=True)
   
    class Meta:
        """ Order bookings by date """
        ordering = ["-date"]
        unique_together = ['date', 'time']

    def __str__(self):
      return f"{self.user.username} - {self.date} - {self.time}"