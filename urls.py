from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("update", views.update, name="update"),
    path("select", views.select, name="select"),
    path("delete", views.delete, name="delete"),
    path("insert", views.insert, name="insert"),
    path("todos/", views.ToDoListCreateView.as_view(), name="todo-list-create"),
    path(
        "todos/<int:pk>/",
        views.ToDoRetrieveUpdateDestroyView.as_view(),
        name="todo-retrieve-update-destroy",
    ),
]
