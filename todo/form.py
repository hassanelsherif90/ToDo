from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class meta:
        model = Todo
        fields = "__all__"