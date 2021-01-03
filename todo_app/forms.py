from django import forms
from django.forms import ModelForm
from django.forms.widgets import DateInput
from .models import Todo


class DateInput(forms.DateInput):
    input_type = 'date'

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['assignment', 'completed', 'due']
        widgets = {
            'due': DateInput(format='%d/%m/%Y %H:%i'),
        }
