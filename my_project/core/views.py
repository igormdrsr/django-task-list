from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Task
from .forms import TaskForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


# def task_list(request):
#     tasks = Task.objects.all()

#     context = {
#         "tasks": tasks
#     }

#     return render(request, "task_list.html", context)


# class TaskListView(ListView):
#     model = Task
#     template_name = "task_list.html"
#     context_object_name = "tasks"


class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()
        form = TaskForm()

        context = {"tasks": tasks, "form": form}
        return render(request, "task_list.html", context)

    def post(self, request):
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("task-list")

        tasks = Task.objects.all()
        return render(request, "task_list.html", {"tasks": tasks, "form": form})


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")


def complete_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        task.is_done = True
        task.save()
    #task-list é o nome da url definida em urls.py
    return redirect("task-list")
