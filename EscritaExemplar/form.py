from logging import PlaceHolder
from django.forms import ModelForm
from django import forms
from .models import Usuario, Redacao, Imagem, CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm




class UsuarioForm(UserCreationForm):
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
            'titulo' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título' }),
            'redacao' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Redacao' }),
            'data_publicacao' : forms.DateInput(attrs={'class': 'form-control'}),
            #Como colocar usuário sendo ele uma chave estrangeira#
        }

class RedacaoSearchForm(forms.Form):
    titulo = forms.CharField(
        label='Título',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Título'}),
    )

# Register your models here.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Imagem  # Certifique-se de importar seu modelo de imagem

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Imagem


from django.contrib.auth.models import User
from django.contrib.auth import forms

# Register your models here.
class CustomUserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = forms.UserCreationForm.Meta.fields + ('email','first_name','last_name',)

    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'form-control'


# forms.py
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UserProfileForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']