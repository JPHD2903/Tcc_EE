from django.shortcuts import render,get_object_or_404,redirect
from .models import Usuario
from .form import UsuarioForm
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
from .form import UsuarioSearchForm
from django.http import HttpResponse






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


#---------------------------------------------------------#

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

class PerfilUpdateView(LoginRequiredMixin, UsuarioUpdateView):
    model = Usuario
    template_name = 'usuario/editar.html'  # Crie este template
    fields = ['nome', 'username', 'email', 'password']  # Campos que podem ser atualizados
    success_url = reverse_lazy('usuarios-profile')  # URL de sucesso após a atualização

    def get_object(self, queryset=None):
        return self.request.use

class PerfilDeleteView(LoginRequiredMixin, UsuarioDeleteView):
    model = Usuario
    template_name = 'usuario/editar.html'  # Crie este template
    success_url = reverse_lazy('usuarios-profile')  # URL de sucesso após a exclusão

    def get_object(self, queryset=None):
        return self.request.user  # Obtém o objeto do






