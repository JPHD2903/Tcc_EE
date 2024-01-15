from django.forms.models import BaseModelForm
from django.shortcuts import render,get_object_or_404,redirect
from .models import Usuario, Redacao
from .form import UsuarioForm, RedacaoForm
from django.views import View
from django.views.generic import ListView
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.paginator import Paginator, Page
from allauth.account.views import LoginView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect
from .form import UsuarioSearchForm, RedacaoSearchForm
from django.http import HttpResponse
from django.contrib.auth import forms

class IndexView(View):
    template_name = "EscritaExemplar/index.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_active:
            return redirect('erro')
        return super().dispatch(request,*args, **kwargs)

    def get(self, request, *args, **kwargs):
        total_usuarios = Usuario.objects.count()

        context = {
            'total_usuarios': total_usuarios,
        }
        return render(request, self.template_name, context)

''''class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'EscritaExemplar/index.html')'''

#---------------------------------------------------------#
class UsuarioListView(ListView):
    model = Usuario
    template_name = "usuario/usuarios.html"
    context_object_name = 'usuarios'
    items_per_page = 4

    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()

        # Processar a pesquisa
        search_form = UsuarioSearchForm(request.GET)
        if search_form.is_valid():
            nome = search_form.cleaned_data.get('nome')
            if nome:
                usuarios = usuarios.filter(nome__icontains=nome)

        paginator = Paginator(usuarios, self.items_per_page)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

        context = {
            'usuarios': page,
            'search_form': search_form,
        }
        return render(request, self.template_name, context)



class UsuarioProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'usuario/perfil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario_logado'] = self.request.user
        return context

ListView
#---------------------------------------------------------#
# views.py
from django.shortcuts import render, redirect
from django.views import View
from .form import CustomUserCreationForm
from django.contrib import messages

class CustomRegisterView(View):
    template_name = "registration/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_valid = False
            user.save()
            messages.success(request, 'Registrado. Agora faça o login para começar!')
            return redirect('index')  # Substitua 'index' pelo nome correto da sua página inicial

        else:
            print('Invalid registration details')

        return render(request, self.template_name, {"form": form})



# views.py
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

class UsuarioCreateView(generic.CreateView):
  model = Usuario
  form_class = UsuarioForm
  success_url = reverse_lazy('index')
  template_name = "usuario/form.html"
  
  def form_valid(self, form):  
    messages.success(self.request, 'Cadastro realizado com sucesso!')
    return super().form_valid(form)


#---------------------------------------------------------#

class UsuarioUpdateView(generic.UpdateView):
  model = Usuario
  form_class = UsuarioForm
  success_url = reverse_lazy("usuarios-list")
  template_name = "usuario/editar.html"


#---------------------------------------------------------#
 
class UsuarioDeleteView(generic.DeleteView):
    model = Usuario
    template_name = 'usuario/usuarios.html'
    success_url = reverse_lazy("usuarios-list")

    def delete(self, request):
        messages.success(self.request, 'Item excluído com sucesso.')
        return super().delete(request)

class UsuarioDeleteView(generic.DeleteView):
    model = Usuario
    template_name = 'usuario/usuarios.html'
    success_url = reverse_lazy("usuarios-list")

    def delete(self, request, *args, **kwargs):
        # Obter o objeto Usuario a ser excluído
        usuario = self.get_object()

        # Excluir o usuário
        usuario.delete()

        # Adicionar uma mensagem de sucesso

        # Redirecionar para a mesma página
        return HttpResponse(reverse_lazy("usuarios-list"))
    
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.shortcuts import render

class UserListView(ListView):
    model = User
    template_name = 'usuario/usuarios.html'  # Substitua com o nome do seu template
    context_object_name = 'users'

# Adicione esta view às suas URLs


#---------------------------------------------------------#


class UsuarioDetailView(generic.DetailView):
    model = Usuario
    template_name = 'usuario/detalhe.html'
    context_object_name = 'usuario'

    def get_object(self, queryset=None):
        item_id = self.kwargs.get('pk')  
        return get_object_or_404(Usuario, pk=item_id)

class CustomLoginView(LoginView):
    def form_valid(self, form):
        # Adicione seu código personalizado aqui
        return super(CustomLoginView, self).form_valid(form)

# views.py
# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .form import UserProfileForm
from django.contrib.auth.models import User 

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'usuario/editar.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('usuarios-profile')

    def get_object(self, queryset=None):
        return self.request.user





class PerfilDeleteView(LoginRequiredMixin, UsuarioDeleteView):
    model = Usuario
    template_name = 'usuario/excluir_perfil.html'  # Crie um template específico para exclusão
    success_url = reverse_lazy('login')


    def get_object(self, queryset=None):
        return self.request.user  # Obtém o objeto do
    
#-------------------------------------------------------------#
#---------------------------Redação---------------------------#
#-------------------------------------------------------------#

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import RedacaoForm  # Importe o formulário associado ao modelo Redacao
import requests
import json
from .utils import enviar_redacao_para_correcao, identificar_erros_redacao

class RedacaoCreateView(LoginRequiredMixin, View):
    template_name = 'redacao/escrever.html'
    form_class = RedacaoForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            redacao = form.save(commit=False)
            redacao.autor = request.user
            redacao.save()

            # Envia a redação para correção
            redacao_corrigida = enviar_redacao_para_correcao(redacao.redacao)

            # Salva a redação corrigida no objeto Redacao
            redacao.redacao_corrigida = redacao_corrigida
            redacao.save()

            return render(request, 'redacao/redacao_corrigida.html', {'redacao': redacao})
            # Pode ajustar a renderização conforme necessário

        return render(request, self.template_name, {'form': form})
    
    def post2(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            redacao = form.save(commit=False)
            redacao.autor = request.user
            redacao.save()

            # Envia a redação para correção
            erros_redacao = identificar_erros_redacao(redacao.redacao)

            # Salva a redação corrigida no objeto Redacao
            redacao.erros_redacao = erros_redacao
            redacao.save()

            return render(request, 'redacao/redacao_corrigida.html', {'redacao': redacao})
            # Pode ajustar a renderização conforme necessário

        return render(request, self.template_name, {'form': form})

    


from django.db.models import Q
# views.py
from django.shortcuts import render
from django.views import View
from .models import Redacao

class SuggestionsView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        redacoes = Redacao.objects.filter(autor=request.user, titulo__icontains=query)
        return render(request, 'redacao/suggestions.html', {'redacoes': redacoes})

# Adicione uma nova view para listar as redações do usuário
class RedacaoListView(LoginRequiredMixin, ListView):
    model = Redacao
    template_name = "redacao/redacoes.html"
    context_object_name = 'redacoes'
    items_per_page = 4

    def get_queryset(self):
        # Obtém o termo de busca do parâmetro 'q' na URL
        query = self.request.GET.get('q')

        # Filtra as redações do usuário atual
        redacoes = Redacao.objects.filter(autor=self.request.user)

        # Se houver um termo de busca, filtra também pelo título
        if query:
            redacoes = redacoes.filter(Q(titulo__icontains=query))

        return redacoes

    def get(self, request, *args, **kwargs):
        redacoes = self.get_queryset()
        return render(request, self.template_name, {'redacoes': redacoes})




class RedacaoDetailView(generic.DetailView):
    model = Redacao
    template_name = 'redacao/detalhe.html'
    context_object_name = 'redacao'

    def get_object(self, queryset=None):
        item_id = self.kwargs.get('pk')  
        return get_object_or_404(Redacao, pk=item_id)
    
class RedacaoDeleteView(generic.DeleteView):
    model = Redacao
    template_name = 'redacao/redacoes.html'
    success_url = reverse_lazy("redacao-list")

    def delete(self, request):
        messages.success(self.request, 'Item excluído com sucesso.')
        return super().delete(request)

class UsuarioDeleteView(generic.DeleteView):
    model = Usuario
    template_name = 'usuario/usuarios.html'
    success_url = reverse_lazy("usuarios-list")

    def delete(self, request, *args, **kwargs):
        # Obter o objeto Usuario a ser excluído
        usuario = self.get_object()

        # Excluir o usuário
        usuario.delete()

        # Adicionar uma mensagem de sucesso

        # Redirecionar para a mesma página
        return HttpResponse(reverse_lazy("usuarios-list"))

#-------------------------------------------------------#
    #---------------API----------------------------#


from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Redacao
from .form import RedacaoForm
import requests
import json

class RedacaoCorrecaoView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        redacao_id = self.kwargs.get('pk')  # Obtém o ID da redação a ser corrigida
        redacao = Redacao.objects.get(pk=redacao_id)

        API_KEY = "sua_chave_do_GPT-3"
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        link = "https://api.openai.com/v1/chat/completions"
        id_modelo = "gpt-3.5-turbo"

        # Cria a mensagem para enviar à API do GPT-3
        body_mensagem = {
            "model": id_modelo,
            "messages": [
                {"role": "user", "content": f"Corrija os erros gramaticais e coesivos da redação", "role": "system"},
                {"role": "user", "content": redacao.texto},  # Adiciona o conteúdo da redação
            ]
        }

        body_mensagem = json.dumps(body_mensagem)

        # Envia a redação para a API do GPT-3
        resposta_api = requests.post(link, headers=headers, data=body_mensagem)

        if resposta_api.status_code == 200:
            resposta = resposta_api.json()
            redacao_corrigida = resposta["choices"][0]["message"]["content"]

            # Salva a redação corrigida no banco de dados
            redacao.corrigida = redacao_corrigida
            redacao.save()

            return JsonResponse({'mensagem': 'Redação enviada e corrigida com sucesso.'})
        else:
            return JsonResponse({'mensagem': 'Erro ao enviar a redação para correção.'}, status=500)
    

    


''''
class InformarRedacaoView(View):
    
    template_name = 'redacao/escrever.html'
    form_class = RedacaoForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            redacao = form.cleaned_data['redacao']
            request.session['redacao'] = redacao  # Armazenar a redação na sessão
            return redirect('redacao_corrigida')
        return render(request, self.template_name, {'form': form})


class RedacaoCorrigidaView(View):
    template_name = 'redacao/redacao_corrigida.html'

    def get(self, request, *args, **kwargs):
        redacao = request.session.get('redacao', '')
        if not redacao: 
            return redirect('escrever')

        redacao_corrigida = enviar_redacao_para_correcao(redacao)
        return render(request, self.template_name, {'redacao_corrigida': redacao_corrigida})

        
'''
    


'''
class CriarRedacaoView(View):
    template_name = 'redacao/escrever.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        redacao = Redacao.objects.create()  # Criar uma nova redação
        return redirect('informar_redacao', pk=redacao.pk)

class InformarRedacaoView(View):
    template_name = 'redacao/informar_redacao.html'
    form_class = RedacaoForm

    def get(self, request, *args, **kwargs):
        redacao_pk = self.kwargs.get('pk')
        redacao = Redacao.objects.get(pk=redacao_pk)
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'redacao': redacao})

    def post(self, request, *args, **kwargs):
        redacao_pk = self.kwargs.get('pk')
        redacao = Redacao.objects.get(pk=redacao_pk)
        form = self.form_class(request.POST)
        if form.is_valid():
            redacao.texto = form.cleaned_data['redacao']
            redacao.save()
            return redirect('corrigir_redacao', pk=redacao.pk)
        return render(request, self.template_name, {'form': form, 'redacao': redacao})

class CorrigirRedacaoView(View):
    template_name = 'redacao/corrigir_redacao.html'

    def get(self, request, *args, **kwargs):
        redacao_pk = self.kwargs.get('pk')
        redacao = Redacao.objects.get(pk=redacao_pk)
        # Lógica para corrigir redação e apresentar resultados
        return render(request, self.template_name, {'redacao': redacao})

'''

'''
class RedacaoListView(ListView):
    model = Redacao
    template_name = "redacao/redacoes.html"
    context_object_name = 'redacoes'
    items_per_page = 4

    def get(self, request, *args, **kwargs):
        redacoes = Redacao.objects.all()

        # Processar a pesquisa
        search_form = RedacaoSearchForm(request.GET)
        if search_form.is_valid():
            titulo = search_form.cleaned_data.get('titulo')
            if titulo:
                redacoes = redacoes.filter(titulo__icontains=titulo)

        paginator = Paginator(redacoes, self.items_per_page)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

        context = {
            'redacoes': page,
            'search_form': search_form,
        }
        return render(request, self.template_name, context)
'''