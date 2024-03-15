from django.db import models
from djrichtextfield.models import RichTextField
from cloudinary.models import CloudinaryField



# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(max_length=10000, null=False, blank=False)
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title