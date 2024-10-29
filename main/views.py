from django.shortcuts import render
from .models import Task

def listar_tarefa(request):
    tarefa = Task.objects.all()
    return render(request, 'tarefa/lista_tarefa.html', {'tarefa1':tarefa})
