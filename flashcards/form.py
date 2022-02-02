from django.forms import ModelForm, Textarea
from .models import FlashCard, Category
from django import forms

class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"
    
class FlashCardForm(ModelForm):
    class Meta:
        model = FlashCard
        exclude = ('id','user')


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        exclude = "__all__"
