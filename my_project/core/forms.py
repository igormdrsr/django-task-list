from django import forms
from .models import Task

from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "category"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "mt-1 w-full border-2 rounded-xs border-slate-300 px-2 py-1",
                    "placeholder": "Ex: Comprar ingredientes",
                    "id": "title-input",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "mt-1 w-full border-2 rounded-xs border-slate-300 px-2 py-1",
                    "placeholder": "Descreva a tarefa...",
                    "rows": 3,
                    "id": "description-input",
                }
            ),
            "category": forms.TextInput(
                attrs={
                    "class": "mt-1 w-full border-2 rounded-xs border-slate-300 px-2 py-1",
                    "placeholder": "Ex: Trabalho, Pessoal...",
                    "id": "category-input",
                }
            ),
        }

class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label = "Usuário",
        widget=forms.TextInput(
            attrs={
                "class": "mt-1 w-full border-2 rounded-xs border-slate-300 px-2 py-1",
                "placeholder": "Digite seu nome de usuário",
                "id": "username-input",
            }
        )
    )

    password  = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "mt-1 w-full border-2 rounded-xs border-slate-300 px-2 py-1",
                "placeholder": "Digite sua senha",
                "id": "password-input",
            }
        ),
        label="Senha"
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "mt-1 w-full border-2 rounded-xs border-slate-300 px-2 py-1",
                "placeholder": "Confirme sua senha",
                "id": "confirm-password-input",
            }
        ),
        label = "Confirmar senha"
    )
    
    def clean(self):
        #Validações padrões do Django. Essas validações são feitas  antes de qualquer outro método de limpeza específico, como clean_username ou clean_password.
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError({"password": "As senhas não coincidem."})
        
        return cleaned_data
    
    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError({"username": "Nome de usuário já existe."})
        
        return username

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label = "Usuário",
        widget=forms.TextInput(
            attrs={
                "class": "mt-1 w-full border-2 rounded-xs border-slate-300 px-2 py-1",
                "placeholder": "Digite seu nome de usuário",
                "id": "username-input",
            }
        )
    )

    password  = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "mt-1 w-full border-2 rounded-xs border-slate-300 px-2 py-1",
                "placeholder": "Digite sua senha",
                "id": "password-input",
            }
        ),
        label="Senha"
    )