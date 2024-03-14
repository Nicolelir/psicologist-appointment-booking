from django.db import models

from djrichtextfield.models import RichTextField


# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(max_length=10000, null=False, blank=False)

    def __str__(self):
        return self.title

class Services(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(max_length=10000, null=False, blank=False)
    
    class Meta:
        db_table = 'services'  # Specify the custom table name
    def __str__(self):
        return self.title