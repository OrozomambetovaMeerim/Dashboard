from django.shortcuts import render
from core.models import Task


def homepage(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "homepage.html", context)
