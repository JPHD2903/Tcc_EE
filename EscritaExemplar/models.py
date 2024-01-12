from django.contrib.auth.models import User 
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    groups = models.ManyToManyField('auth.Group', related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_set', blank=True)

class Imagem(models.Model):
    arquivo = models.ImageField(upload_to='imgs/')

    def __str__(self):
        return self.arquivo.name

class Redacao(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    redacao = models.TextField()
    redacao_corrigida = models.TextField(blank=True, null=True)
    erros_redacao = models.TextField(blank=True, null=True)  
    data_publicacao = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titulo
    
class Usuario(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)







    

