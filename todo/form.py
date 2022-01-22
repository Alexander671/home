from django.forms import ModelForm
from .models import TodoList

class ToDoListForm(ModelForm):
    class Meta:
        model = TodoList
        fields = ["title","content", "due_date", "category" ]