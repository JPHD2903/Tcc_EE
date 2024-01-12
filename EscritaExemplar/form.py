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

class CustomUserCreationForm(UserCreationForm):
    profile_picture = forms.ModelChoiceField(
        queryset=Imagem.objects.all(),
        empty_label="Escolha uma imagem",
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name', 'profile_picture',)


# forms.py
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UserProfileForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']