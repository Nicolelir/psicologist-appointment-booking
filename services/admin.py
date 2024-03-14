from django.contrib import admin
from .models import About, Services


# Register your models here.
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
  list_display = ('title', 'content')
   

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
   list_display = ('title', 'description')
   
