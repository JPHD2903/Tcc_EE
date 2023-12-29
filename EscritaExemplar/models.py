from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    
class Redacao(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    redacao = models.TextField()
    modalidade = models.CharField(max_length=50)
    data_publicacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo


    

