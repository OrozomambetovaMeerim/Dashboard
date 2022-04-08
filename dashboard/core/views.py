from django.shortcuts import render, redirect
from core.models import Task
from django.views.decorators.http import require_http_methods


def homepage(request):
    tasks_1 = Task.objects.filter(status=1)
    tasks_2 = Task.objects.filter(status=2)
    tasks_3 = Task.objects.filter(status=3)
    context = {}
    context["tasks_1"] = tasks_1
    context["tasks_2"] = tasks_2
    context["tasks_3"] = tasks_3
    return render(request, "homepage.html", context)

@require_http_methods(["POST"])
def add(request):
    text = request.POST.get("task_text")
    Task(text=text).save()
    return redirect(homepage)


def status(request, id):
    task = Task.objects.get(id=id)
    task.status += 1
    task.save()
    return redirect(homepage)
