from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')


@login_required(login_url='account_login')
def todos(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos.html', context)


@login_required(login_url='account_login')
def todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    context = {
        'todo': todo
    }
    return render(request, 'todo.html', context)


@login_required(login_url='account_login')
def create_todo(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('todos')
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


@login_required(login_url='account_login')
def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos')
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


@login_required(login_url='account_login')
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        todo.delete()
        return redirect('todos')
    return render(request, 'delete.html', {'todo': todo})
