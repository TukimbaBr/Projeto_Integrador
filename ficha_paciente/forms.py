from django import forms
from .models import Idoso, estado_choices, Foto

class IdosoForm(forms.ModelForm):
    class Meta:
        model = Idoso
        fields = "__all__"
        exclude = ['slug']

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['foto']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.foto:
            self.fields['foto'].widget.attrs['src'] = self.instance.foto.url




