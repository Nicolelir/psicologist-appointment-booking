from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'created_on', 'status', 'approved']
    list_filter = ['status', 'approved']
    search_fields = ['author', 'text']
    date_hierarchy = 'created_on'
    ordering = ['-created_on']

admin.site.register(Review, ReviewAdmin)