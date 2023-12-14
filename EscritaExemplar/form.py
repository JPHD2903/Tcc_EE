from django.forms import ModelForm
from django import forms
from .models import Usuario, Redacao


class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome' }),
            'nickname' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de usuário' }),
            'email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email' }),
            'senha': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'})    
        }

   
class RedacaoForm(ModelForm):

    class Meta:
        model = Redacao
        fields = '__all__'
        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control' }),
            'texto' : forms.TextInput(attrs={'class': 'form-control' }),
            'modalidade' : forms.TextInput(attrs={'class': 'form-control' }),
            'data_publicacao' : forms.DateInput(attrs={'class': 'form-control'}),
            #Como colocar usuário sendo ele uma chave estrangeira#
        }

class UsuarioSearchForm(forms.Form):
    nome = forms.CharField(label='Nome', required=False)
