from django.db import models

class Task(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField(blank=True)
    genero = models.CharField(max_length=1)
    data = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nome