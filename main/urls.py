from django.contrib import admin
from django.urls import path, include
from EscritaExemplar.views import IndexView, UsuarioListView, UsuarioProfileView,UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView, UsuarioDetailView
from EscritaExemplar.views import RedacaoDetailView , RedacaoDeleteView, RedacaoCreateView, RedacaoListView
from EscritaExemplar.views import UserProfileUpdateView , PerfilDeleteView, CustomRegisterView, RedacaoCorrecaoView

from django.views import generic
from allauth.account.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    #path('accounts/', include('allauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', IndexView.as_view(), name='index'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    #path('accounts/login/', LoginView.as_view(), name='account_login'),
    #path('accounts/logout/', LogoutView.as_view(), name='account_logout'),

    #USUÁRIO#
    path('usuario/',UsuarioCreateView.as_view(),name='criar_usuario'),
    path('usuario/listar',UsuarioListView.as_view(),name='usuarios-list'),
    path('usuario/perfil',UsuarioProfileView.as_view(),name='usuarios-profile'),
    path('usuario/editar/<int:pk>/', UsuarioUpdateView.as_view(), name='usuarios-update'),
    path('usuario/delete/<int:pk>/', UsuarioDeleteView.as_view(), name='usuarios-delete'),
    path('usuario/detalhe/<int:pk>/', UsuarioDetailView.as_view(), name='usuarios-detail'),
    #PERFIL#
    path('perfil/editar/', UserProfileUpdateView.as_view(), name='profile-update'),
    path('perfil/delete/<int:pk>/', PerfilDeleteView.as_view(), name='profile-delete'),
    #REDAÇÃO#
    path('redacao/criar', RedacaoCreateView.as_view(), name='criar_redacao'),
    path('redacao/listar',RedacaoListView.as_view(),name='redacao-list'),
    path('redacao/delete/<int:pk>/', RedacaoDeleteView.as_view(), name='redacao-delete'),
    path('redacao/detalhe/<int:pk>/', RedacaoDetailView.as_view(), name='redacao-detail'),

    path('redacao/correcao/<int:pk>/', RedacaoCorrecaoView.as_view(), name='redacao-correcao'),
    #path('escrever/', InformarRedacaoView.as_view(), name='criar_redacao'),
    #path('redacao/redacao_corrigida', RedacaoCorrigidaView.as_view(), name='redacao_corrigida'),
   

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    
]