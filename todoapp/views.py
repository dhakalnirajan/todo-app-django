from django.shortcuts import render, redirect
from django.http import HttpResponse
from todoapp.models import TODOAPP


# Create your views here.
def make_complete(request, pk):
    task = TODOAPP.objects.get(pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def delete(request, pk):
    task = TODOAPP.objects.get(pk=pk)
    task.delete()
    return redirect('home')

def add_task(request):
    task = request.POST['task']
    TODOAPP.objects.create(task_name=task)
    return redirect('home')

def clear_completed(request):
    # Delete all completed tasks
    TODOAPP.objects.filter(is_completed=True).delete()
    return redirect('home')