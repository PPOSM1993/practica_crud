from django.forms import ModelForm
from .models import *

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('date',)