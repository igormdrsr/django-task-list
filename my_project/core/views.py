from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Task
from .forms import LoginForm, TaskForm, RegisterForm


# Create your views here.
class TaskListView(LoginRequiredMixin, View):
    def get(self, request):
        tasks = Task.objects.filter(user=request.user)

        context = {"tasks": tasks}
        return render(request, "task_list.html", context)

class CompleteTaskView(View):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id, user=request.user)
        task.is_done = True
        task.save()
        return redirect("task_list")

class CreateTaskView(LoginRequiredMixin, View):
    def get(self, request):
        form = TaskForm()

        context = {"form": form}
        return render(request, "create_task.html", context)

    def post(self, request):
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task_list")

        context = {"form": form}
        return render(request, "create_task.html", context)


class UpdateTaskView(LoginRequiredMixin, View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id, user=request.user)
        form = TaskForm(instance=task)

        context = {"form": form}
        return render(request, "update_task.html", context)

    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id, user=request.user)
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("task_list")

        context = {"form": form}
        return render(request, "update_task.html", context)


class RegisterView(View):
    def get(self, request):
        context = {"form": RegisterForm()}
        return render(request, "register.html", context)

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )

            return redirect("login")
        context = {"form": form}
        return render(request, "register.html", context)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {"form": form}
        return render(request, "login.html", context)

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect("task_list")
            
            form.add_error(None, "Invalid username or password.")

        context = {"form": form}
        return render(request, "login.html", context)
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")
