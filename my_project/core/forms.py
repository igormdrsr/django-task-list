from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "category"]
        # widgets = {
        #     "title": forms.TextInput(
        #         attrs={
        #             "class": "w-full rounded-md border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
        #             "placeholder": "Ex: Comprar ingredientes",
        #         }
        #     ),
        #     "description": forms.Textarea(
        #         attrs={
        #             "class": "w-full rounded-md border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
        #             "placeholder": "Descreva a tarefa...",
        #             "rows": 3,
        #         }
        #     ),
        #     "category": forms.TextInput(
        #         attrs={
        #             "class": "w-full rounded-md border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
        #             "placeholder": "Ex: Trabalho, Pessoal...",
        #         }
        #     ),
        # }
