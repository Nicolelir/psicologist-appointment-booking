
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField
from bookings.models import Booking
from services. models import Services
from bookings. models import Booking

# Create your models here.

SERVICES_TYPES= (("online individual therapy", "Online Individual Therapy"), ("online family therapy", "Online Family Therapy"), ("workshop", "Workshop"))
# Create your models here.

class Review(models.Model):
    """
    A model for leaving reviews
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name="reviews",  default=1)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="booking",  default=1)
    created_on = models.DateTimeField(default=datetime.now)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1)
    text = models.TextField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Review by {self.author.username} on {self.created_on}"