from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def index(request):
    todos = ToDo.objects.filter(title__contains = request.GET.get('search', ''))
    context = {
        'todos': todos
    }
    return render(request, 'todo/index.html', context)

def view(request, id):
    todo = ToDo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'todo/detail.html', context)

def create(request):
    if request.method == 'GET':
        form = TodoForm()
        context = {
            'form': form
        }
        return render(request, 'todo/create.html', context)
    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save() 
        return redirect('todo')
    
    

def edit(request, id):
    contact = ToDo.objects.get(id=id)
    
    if request.method == 'GET':
        form = TodoForm(instance=contact)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'todo/edit.html', context)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
            'id': id
        }
        messages.success(request, 'Tarea Actualizada.')
        return render(request, 'todo/edit.html', context)



def delete(request, id):
    todo  = ToDo.objects.get(id=id)
    todo.delete()
    return redirect('todo')