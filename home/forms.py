from django import forms
from .models import Contact

class FooterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['email'].initial = user.email  # Set initial value of the author field to user's email
        self.fields['name'].required = True
        self.fields['email'].required = True
        self.fields['query'].required = True

        self.fields['name'].label = "Name"
        self.fields['email'].label = "Email"
        self.fields['query'].label = "Query"
     
    class Meta:
        model = Contact
        fields = ['name', 'email', 'query']
