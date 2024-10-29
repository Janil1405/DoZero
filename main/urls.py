from django.contrib import admin
from django.urls import path
from .views import listar_tarefa

urlpatterns=[
    path('', listar_tarefa, name='listar_tarefa')
]