from django import template
from ficha_paciente.models import Foto

register = template.Library()

@register.filter(name='get_first_image')
def get_first_image(senhor):
    imagem = Foto.objects.filter(idoso=senhor).first()
    if imagem:
        return imagem.foto.url
    else:
        return False