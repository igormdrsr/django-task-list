from django.urls import path
from . import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task_list"),
    path("login", views.LoginView.as_view(), name="login"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("complete/<int:task_id>/", views.CompleteTaskView.as_view(), name="complete_task"),
    path("create", views.CreateTaskView.as_view(), name="create_task"),
    path("update/<int:task_id>/", views.UpdateTaskView.as_view(), name="update_task")
]
