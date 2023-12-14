from django.contrib import admin
from django.urls import path, include
from EscritaExemplar.views import IndexView, UsuarioListView, UsuarioProfileView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView, UsuarioDetailView
#from EscritaExemplar.views import StandListView, StandCreateView, StandUpdateView, StandDeleteView, StandDetailView
from django.views import generic
from allauth.account.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', IndexView.as_view(), name='index'),
    path('accounts/login/', LoginView.as_view(), name='account_login'),
    #path('accounts/logout/', LogoutView.as_view(), name='account_logout'),

    path('usuario/',UsuarioCreateView.as_view(),name='criar_usuario'),
    path('usuario/listar',UsuarioListView.as_view(),name='usuarios-list'),
     path('usuario/perfil',UsuarioProfileView.as_view(),name='usuarios-profile'),
    path('usuario/editar/<int:pk>/', UsuarioUpdateView.as_view(), name='usuarios-update'),
    path('usuario/delete/<int:pk>/', UsuarioDeleteView.as_view(), name='usuarios-delete'),
    path('usuario/detalhe/<int:pk>/', UsuarioDetailView.as_view(), name='usuarios-detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]