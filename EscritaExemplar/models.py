from django.contrib.auth.models import User 
from django.db import models


#from django.contrib.auth.models import AbstractUser


class Redacao(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    redacao = models.TextField()
    redacao_corrigida = models.TextField(blank=True, null=True)  
    data_publicacao = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titulo
    
class Usuario(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)







    

