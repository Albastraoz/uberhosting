from django import forms
from .models import Contact

# Contact form model
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name', 'email', 'message')
