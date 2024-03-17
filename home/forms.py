from django import forms
from .models import Contact


class FooterForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'query')