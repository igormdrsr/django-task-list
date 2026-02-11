from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "category"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "mt-1 w-full border-2 rounded-xs border-slate-300 px-2 py-1",
                    "placeholder": "Ex: Comprar ingredientes",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "mt-1 w-full border-2 rounded-xs border-slate-300 px-2 py-1",
                    "placeholder": "Descreva a tarefa...",
                    "rows": 3,
                }
            ),
            "category": forms.TextInput(
                attrs={
                    "class": "mt-1 w-full border-2 rounded-xs border-slate-300 px-2 py-1",
                    "placeholder": "Ex: Trabalho, Pessoal...",
                }
            ),
        }
