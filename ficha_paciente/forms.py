from django import forms
from .models import Idoso

class IdosoForm(forms.ModelForm):
    class Meta:
        model = Idoso
        fields = "__all__"
        