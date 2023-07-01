from django.shortcuts import render
from django.shortcuts import redirect

from myapp.models import ToDo
from rest_framework import generics
from .serializers import ToDoSerializer


class ToDoListCreateView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


# Create your views here.
def index(request):
    todos = ToDo.objects.all()
    context = {"todos": todos}
    return render(request, "index.html", context)


def delete(request):
    id = request.POST.get("id")
    selected = ToDo.objects.get(id=id)
    selected.delete()
    return redirect("index")


def select(request):
    if request.method == "POST":
        id = request.POST.get("id")
        selected = ToDo.objects.get(id=id)
        context = {"selected": selected}
        return render(request, "update.html", context)


def insert(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")
        tags = request.POST.get("tags")
        status = request.POST.get("status")
        data = ToDo(
            title=title,
            description=description,
            due_date=due_date,
            tags=tags,
            status=status,
        )
        data.save()
    return redirect("index")


def update(request):
    if request.method == "POST":
        id = request.POST.get("id")
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")
        tags = request.POST.get("tags")
        status = request.POST.get("status")
        todo = ToDo.objects.get(id=id)
        todo.title = title
        todo.description = description
        todo.due_date = due_date
        todo.tags = tags
        todo.status = status
        todo.save()
    return redirect("index")
