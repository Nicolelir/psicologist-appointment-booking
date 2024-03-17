
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField
from bookings.models import Booking
from services. models import Services

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

DEFAULT_CHOICES = (
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
    ('1', '1'),
)

SERVICES_TYPES= (("online individual therapy", "Online Individual Therapy"), ("online family therapy", "Online Family Therapy"), ("workshop", "Workshop"))
# Create your models here.

class Review(models.Model):
    """
    A model for leave reviews
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_review")
    created_on = models.DateTimeField(auto_now_add=True)
    services = models.ForeignKey(Services, on_delete=models.CASCADE, related_name="type_service")
    text =  models.TextField()
    rating_value = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return str(self.author)

    def rating(self):
        return self.rating_value

  