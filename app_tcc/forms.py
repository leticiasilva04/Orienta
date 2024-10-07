from django import forms
from .models import Teste

class TesteForm(forms.ModelForm):
    class Meta:
        model = Teste
        fields = ('titulo', 'capa_tcc', 'autores', 'orientador', 'status', 'data_entrega')