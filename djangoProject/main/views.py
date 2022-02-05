from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.order_by('-id')[:5]
    return render(request, 'main/index.html', {'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    if (request.method == 'POST'):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)