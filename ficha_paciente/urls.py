from django.urls import path
from . import views

urlpatterns = [
    path('add_paciente/', views.add_paciente, name="add_paciente"),
    path('idoso/<slug:slug>', views.idoso, name="idoso"),

]

