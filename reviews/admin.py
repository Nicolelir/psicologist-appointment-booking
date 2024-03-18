from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'created_on', 'text']
    ordering = ['-created_on']

admin.site.register(Review, ReviewAdmin)