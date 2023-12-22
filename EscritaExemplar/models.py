from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
class Redacao(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    redacao = models.TextField()
    modalidade = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_publicacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo


    

