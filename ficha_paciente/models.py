from django.db import models
from django.template.defaultfilters import slugify

estado_choices = [
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espírito Santo"),
    ("GO", "Goiás"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "São Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins")
]

sexo_choices = ("Masculino", "Feminino")

estado_civil_choices = ("Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viúvo(a)", "Separado(a)")

raca_choices = ("Preto(a)", "Pardo(a)", "Branco(a)", "Indígena(a)", "Amarelo(a)")

setor_choices = ("São Carlos", "São Vicente", "Central")


class Idoso(models.Model):
    id_idoso = models.AutoField(primary_key=True, unique=True)
    nome_idoso = models.CharField(max_length=100)
    naturalidade_idoso = models.CharField(max_length=100, blank=True, null=True)
    sexo_idoso = models.CharField(choices=sexo_choices)
    setor_idoso = models.CharField(choices= setor_choices)
    data_nasc_idoso = models.DateField()
    data_adimissao_idoso = models.DateField()
    cpf_idoso = models.CharField(max_length=11, unique=True)
    rg_idoso = models.CharField(max_length=10, unique=True)
    estado_civil_idoso = models.CharField(max_length=20)
    religiao_idoso = models.CharField(max_length=50, blank=True, null=True)
    raca_idoso = models.CharField(choices=raca_choices, blank=True)
    plano_saude_idoso = models.CharField(max_length=100)
    cartao_sus_idoso = models.CharField(max_length=50, unique=True)
    profissao_idoso = models.CharField(max_length=100, blank=True, null=True)
    vinculo_idoso = models.BooleanField(default=False, help_text="O idoso possui vínculo familiar ou social?")

    estado_idoso = models.CharField(choices=estado_choices)
    cidade_idoso = models.CharField(max_length=55, )
    cep_endereco_idoso = models.CharField(max_length=8, blank=True, null = True)
    rua_endereco_idoso = models.CharField(max_length=255, blank=True, null = True)
    numero_endereco_idoso = models.CharField(max_length=10, blank=True, null = True)
    bairro_endereco_idoso = models.CharField(max_length=55, blank=True, null = True)
    complemento_endereco_idoso = models.CharField(max_length=55, blank=True, null = True)
    
    email_idoso = models.EmailField(blank=True, null = True)
    celular_idoso = models.CharField(max_length=11)
    celular_outro_idoso = models.CharField(max_length=11, blank=True, null=True)
    tell_residencial_idoso = models.CharField(max_length=10, blank=True, null=True)
    historia_pregressa_idoso = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.nome_idoso
    
    def save(self, *args, **kwargs):
        if self.nome_idoso:
            slug_candidate = slugify(self.nome_idoso)
            counter = 1
            while Idoso.objects.filter(slug=slug_candidate).exists():
                slug_candidate = f"{slugify(self.nome_idoso)}-{counter}"
                counter += 1
            self.slug = slug_candidate
        else:
            self.slug = None
        
        return super().save(*args, **kwargs)

    
class Foto(models.Model):
    foto = models.ImageField(upload_to="foto_idoso")
    idoso = models.ForeignKey(Idoso, on_delete=models.CASCADE)
