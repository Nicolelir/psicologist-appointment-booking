from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Contact(models.Model):
    """
    Stores a single contact form message
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    query = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact form {self.name}"