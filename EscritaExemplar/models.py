from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
    def __str__(self):
        return self.nickname

class Redacao(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    texto = models.TextField()
    modalidade = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    

