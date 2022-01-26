from django.forms import ModelForm, Textarea
from .models import Request
from django import forms

class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"
    
class RequestForm(ModelForm):
    class Meta:
        model = Request
        exclude = ('id','user', 'response')
        choices = [('ON', 'ON'), ('OFF', 'OFF')]
        
        widgets = {
                'time_request': DateTimeLocalInput(attrs={'type': 'datetime-local'}),
                'url': forms.RadioSelect(choices = choices)
        } 