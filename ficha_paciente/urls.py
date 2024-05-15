from django.urls import path, include
from . import views

urlpatterns = [
    
    path('add_paciente/', views.add_paciente, name="add_paciente"),
    path('idoso/<slug:slug>', views.idoso, name="idoso"),
    path('excluir_idoso/<slug:slug>/', views.excluir_idoso, name='excluir_idoso'),
]

