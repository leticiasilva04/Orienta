from django import forms
from .models import TCC

class TCCForm(forms.ModelForm):
    class Meta:
        model = TCC
        fields = ['titulo', 'capa_tcc', 'descricao', 'curso', 'data_inicio', 'data_entrega', 'status']