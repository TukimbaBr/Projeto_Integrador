from django.shortcuts import render
from .forms import IdosoForm, FotoForm
from .models import  estado_choices, estado_civil_choices, raca_choices, setor_choices, sexo_choices, Idoso, Foto
from django.http import HttpResponse
from PIL import Image, ImageDraw
from datetime import date
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from rolepermissions.decorators import has_permission_decorator
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
import os
from django.conf import settings



@has_permission_decorator('cadastrar_paciente')
def add_paciente(request):
    tab_exibicao = True
    idosos = Idoso.objects.all().order_by('nome_idoso')

    if request.method == "GET":
        nome = request.GET.get('nome')
        data_admissao = request.GET.get('data_admissao')
        sexo = request.GET.get('sexo')
        plano_saude = request.GET.get('plano_saude')
        setor = request.GET.get('setor')


        if nome or data_admissao or sexo or plano_saude or setor:

            if nome:
               idosos =  idosos.filter(nome_idoso__icontains=nome)
            
            if sexo:
               idosos =  idosos.filter(sexo_idoso=sexo)
            
            if plano_saude:
                idosos = idosos.filter(plano_saude_idoso=plano_saude)


            if setor:
               idosos =  idosos.filter(setor_idoso=setor)
            
            if data_admissao:
                idosos = idosos.filter(data_adimissao_idoso__gte=data_admissao)
        
                #inicio do paginator
        add_paciente_paginator = Paginator(idosos, 4)
        page_num = request.GET.get('page')
        page_obj = add_paciente_paginator.get_page(page_num)
        
        return render(request, 'add_paciente.html', {'estado_choices': estado_choices,
                                                    'estado_civil_choices': estado_civil_choices,
                                                    'raca_choices': raca_choices,
                                                    'setor_choices': setor_choices,
                                                    'sexo_choices': sexo_choices,
                                                    'tab_exibicao': tab_exibicao,
                                                    'page_obj': page_obj})
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        data_nasc = request.POST.get('data_nasc')
        naturalidade = request.POST.get('naturalidade')
        sexo = request.POST.get('sexo')
        setor = request.POST.get('setor')
        data_nasc = request.POST.get('data_nasc')
        data_admissao = request.POST.get('data_admissao')
        cpf = request.POST.get('cpf')
        rg = request.POST.get('rg')
        estado_civil = request.POST.get('estado_civil')
        religiao = request.POST.get('religiao')
        raca = request.POST.get('raca')
        plano_saude = request.POST.get('plano_saude')
        cartao_sus = request.POST.get('cartao_sus')
        profissao = request.POST.get('profissao')
        vinculo = request.POST.get('vinculo')
        estado = request.POST.get('estado_idoso')
        cidade = request.POST.get('cidade_idoso')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        complemento = request.POST.get('complemento')
        email = request.POST.get('email')
        celular = request.POST.get('celular_idoso')
        celular_outro = request.POST.get('celular_outro')
        tell_residencial = request.POST.get('tell_residencial')
        historia_pregressa = request.POST.get('historia_pregressa')
       
        #TODO:Mudar o campo Sexo Idoso, usar mesmo sista do estados

        velho = Idoso(nome_idoso=nome,
                        naturalidade_idoso=naturalidade,
                        sexo_idoso = sexo,
                        setor_idoso = setor,
                        data_nasc_idoso = data_nasc,
                        data_adimissao_idoso = data_admissao,
                        cpf_idoso = cpf,
                        rg_idoso = rg,
                        estado_civil_idoso = estado_civil,
                        religiao_idoso = religiao,
                        raca_idoso = raca,
                        plano_saude_idoso = plano_saude,
                        cartao_sus_idoso = cartao_sus,
                        profissao_idoso = profissao,
                        vinculo_idoso = vinculo,

                        estado_idoso = estado,
                        cidade_idoso = cidade,
                        cep_endereco_idoso = cep,
                        rua_endereco_idoso = rua,
                        numero_endereco_idoso = numero,
                        bairro_endereco_idoso = bairro,
                        complemento_endereco_idoso = complemento,
                        
                        email_idoso = email,
                        celular_idoso = celular,
                        celular_outro_idoso = celular_outro,
                        tell_residencial_idoso = tell_residencial,
                        historia_pregressa_idoso = historia_pregressa)
        velho.save()

        for f in request.FILES.getlist('fotos'):
            name = f'{date.today()}_{velho.id_idoso}_{velho.nome_idoso}.jpg'
            img = Image.open(f)
            img = img.convert('RGB')
            img = img.resize((160,160))
            draw = ImageDraw.Draw(img)
            draw.text((20,280), f"Lar Acolhedor Sào Vicente de São Paulo {date.today()}", (255, 255, 0))
            output = BytesIO()
            img.save(output, format="JPEG", quality=100)
            output.seek(0)
            img_final = InMemoryUploadedFile(output, 'ImageField', name, 'image/jpeg', sys.getsizeof(output), None)

            img_dj = Foto(foto= img_final, idoso=velho)
            img_dj.save()
            print('f: ', f)
            print('img: ', img)
            print('img_final: ', img_final)
            print('img_dj: ', img_dj)
        messages.add_message(request, messages.SUCCESS, 'Idoso Cadastrado com Sucesso!')
        return redirect(reverse('add_paciente'))

def idoso(request, slug):
    idoso = Idoso.objects.get(slug=slug)
    foto = Foto.objects.filter(idoso=idoso).first()
    
    if request.method == "POST":
        form_idoso = IdosoForm(request.POST, instance=idoso)
        form_foto = FotoForm(request.POST, request.FILES, instance=foto)
        
        if form_idoso.is_valid() and form_foto.is_valid():
            form_idoso.save()
            
            if 'foto' in request.FILES:
                form_foto.save()
                
            messages.success(request, 'Detalhes do idoso atualizados com sucesso!')
            return redirect('editar_idoso', slug=idoso.slug)
    else:
        form_idoso = IdosoForm(instance=idoso)
        form_foto = FotoForm(instance=foto)
    
    return render(request, 'idosos.html', {'form': form_idoso, 'form_ft': form_foto, 'idoso': idoso})


import os
from django.conf import settings

@has_permission_decorator('cadastrar_funcionarios')
def excluir_idoso(request, slug):
    # Lógica para excluir um idoso
    idoso = get_object_or_404(Idoso, slug=slug)
    
    # Excluindo as fotos associadas ao idoso
    fotos = Foto.objects.filter(idoso=idoso)
    for foto in fotos:
        # Excluindo o arquivo de mídia físico
        if foto.foto:
            foto_path = os.path.join(settings.MEDIA_ROOT, str(foto.foto))
            if os.path.exists(foto_path):
                os.remove(foto_path)
        # Excluindo o registro de foto do banco de dados
        foto.delete()
    
    # Excluindo o idoso
    idoso.delete()
    
    messages.success(request, 'Idoso e mídias relacionadas excluídos com sucesso!')
    return redirect(reverse('add_paciente'))




