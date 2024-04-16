from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_funcionarios/', views.cadastrar_funcionarios, name="cadastrar_funcionarios"),
    path('login/', views.login, name="login"),
    path('sair/', views.logout, name="sair"),
    path('excluir_usuario/<str:id>/', views.excluir_usuario, name="excluir_usuario"),
    path('plataforma/', views.plataforma, name='plataforma')
]
