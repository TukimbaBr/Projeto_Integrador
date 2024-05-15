from django import forms
from .models import Idoso, estado_choices, Foto

class IdosoForm(forms.ModelForm):
    class Meta:
        model = Idoso
        fields = "__all__"
        exclude = ['slug']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_nome'})
        self.fields['naturalidade_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_naturalidade'})
        self.fields['sexo_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_sexo'})
        self.fields['setor_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_setor'})
        self.fields['data_nasc_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_data_nasc'})
        self.fields['data_adimissao_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_data_admissao'})
        self.fields['cpf_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_cpf'})
        self.fields['rg_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_rg'})
        self.fields['estado_civil_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_estado_civil'})
        self.fields['religiao_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_religiao'})
        self.fields['raca_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_raca'})
        self.fields['plano_saude_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_plano_saude'})
        self.fields['cartao_sus_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_cartao_sus'})
        self.fields['profissao_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_profissao'})
        self.fields['vinculo_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_vinculo'})
        self.fields['estado_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_estado'})
        self.fields['cidade_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_cidade'})
        self.fields['cep_endereco_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_cep'})
        self.fields['rua_endereco_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_rua'})
        self.fields['numero_endereco_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_numero'})
        self.fields['bairro_endereco_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_bairro'})
        self.fields['complemento_endereco_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_complemento'})
        self.fields['email_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_email'})
        self.fields['celular_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_celular'})
        self.fields['celular_outro_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_celular_outro'})
        self.fields['tell_residencial_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_tell_residencial'})
        self.fields['historia_pregressa_idoso'].widget.attrs.update({'class': 'form-control', 'id': 'id_historia_pregressa'})

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['foto']
        
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.foto:
            self.fields['foto'].widget.attrs.update({'class': 'form-control', 'id': 'picture__input'})
            




