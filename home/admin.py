from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Contact



# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('query', 'read',)