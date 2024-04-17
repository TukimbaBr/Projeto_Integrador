from django.http import HttpResponse
from django.shortcuts import render
from rolepermissions.decorators import has_permission_decorator
from .models import Users
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.contrib import messages

def plataforma(request):
    if request.method == "GET":
        return render(request, 'plataforma.html')
    
@has_permission_decorator('cadastrar_funcionarios')
def cadastrar_funcionarios(request):
    if request.method == "GET":
        funcionarios = Users.objects.filter(cargo="F")
        return render(request, 'cadastrar_funcionarios.html', {'funcionarios': funcionarios})
    if request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')


        user = Users.objects.filter(email=email)

        if user.exists():
            # TODO: Utilizar mensagens do Django
            return HttpResponse('Email já existe')
        
        user = Users.objects.create_user(username=email,
                                            password=senha,
                                            first_name=nome,
                                            last_name=sobrenome,
                                            cargo="F")

        #TODO: redirecionar com uma mensagem
        return HttpResponse('Conta criada')
    
def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('plataforma'))
        return render(request, 'login.html')
    elif request.method == "POST":
        login = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=login, password=senha)

        if not user:
            #TODO: Redirecionar com mensagem de erro
            return HttpResponse('Usuário inválido')
        
        auth.login(request, user)
        return redirect(reverse('plataforma'))
    
def logout(request):
    request.session.flush()
    return redirect(reverse('login'))

@has_permission_decorator('cadastrar_funcionarios')
def excluir_usuario(request, id):
    funcionario = get_object_or_404(Users, id=id)
    funcionario.delete()
    messages.add_message(request, messages.SUCCESS, 'Funcionàrio Excluído com sucesso')
    return redirect(reverse('cadastrar_funcionarios'))