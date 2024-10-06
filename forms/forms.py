# app_tcc/forms/forms.py

from django import forms
from app_tcc.models import TCC  # Ajuste para o caminho correto

class TCCForm(forms.ModelForm):
    class Meta:
        model = TCC
        fields = [
            'titulo',
            'descricao',
            'capa_tcc',
            'autores',
            'curso',
            'data_inicio',
            'data_entrega',
        ]

    def clean_autores(self):
        autores = self.cleaned_data.get('autores')
        if not autores or len(autores) < 1 or len(autores) > 3:
            raise forms.ValidationError("Selecione entre 1 a 3 autores.")
        return autores
