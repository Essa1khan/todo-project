from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Task


def home(request):
    """Display active and completed tasks on the home page."""
    tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)

    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
    }

    return render(request, 'home.html', context)


def addTask(request):
    """Create a new task and redirect back to the home page."""
    if request.method == "POST":
        task_text = request.POST.get('task', '').strip()
        if task_text:
            Task.objects.create(task=task_text)
    return redirect('home')


def completeTask(request, task_id):
    """Mark the specified task as completed."""
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = True
    task.save()
    return redirect('home')


def deleteTask(request, task_id):
    """Delete the specified task."""
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')


def editTask(request, task_id):
    """Show edit form or save changes for a task."""
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        new_text = request.POST.get('task', '').strip()
        if new_text:
            task.task = new_text
            task.save()
            return redirect('home')
    return render(request, 'edit.html', {'task': task})