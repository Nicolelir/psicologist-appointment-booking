from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField

# Create your models here.
home_image = CloudinaryField('image', default='placeholder')

class Contact(models.Model):
    """
    Stores a single contact form message
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    query = models.TextField()
    date = models.DateField(default=datetime.now, blank=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact form {self.name}"