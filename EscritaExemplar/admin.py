from django.contrib import admin
from .models import Usuario, Redacao

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "username", "email", "password")

@admin.register(Redacao)
class RedacaoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "redacao", "modalidade", "data_publicacao")

