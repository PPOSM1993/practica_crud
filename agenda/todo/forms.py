from django.forms import ModelForm, DateInput
from .models import *

class TodoForm(ModelForm):
    class Meta:
        model = ToDo
        exclude = ('date',)
        widgets = {
            'estimated_end': DateInput(attrs={
                'type': 'date'
            })
        }