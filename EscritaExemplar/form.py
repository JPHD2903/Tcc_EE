from logging import PlaceHolder
from django.forms import ModelForm
from django import forms
from .models import Usuario, Redacao


class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome' }),
            'username' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de usuário' }),
            'email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email' }),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'})    
        }

class UsuarioSearchForm(forms.Form):
    nome = forms.CharField(
        label='Nome',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Nome'}),
    )
    

   
class RedacaoForm(ModelForm):

    class Meta:
        model = Redacao
        fields = '__all__'
        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control' }),
            'redacao' : forms.Textarea(attrs={'class': 'form-control' }),
            'modalidade' : forms.TextInput(attrs={'class': 'form-control' }),
            'data_publicacao' : forms.DateInput(attrs={'class': 'form-control'}),
            #Como colocar usuário sendo ele uma chave estrangeira#
        }

class RedacaoSearchForm(forms.Form):
    titulo = forms.CharField(
        label='Título',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Título'}),
    )

