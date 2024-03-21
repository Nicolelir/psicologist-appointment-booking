from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'query']

