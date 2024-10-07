from django import forms
from .models import TCC
from .models import Teste

class TCCForm(forms.ModelForm):
    class Meta:
        model = TCC
        fields = ['titulo', 'capa_tcc', 'descricao', 'curso', 'data_inicio', 'data_entrega', 'status']from django import forms
from .models import Teste

class TesteForm(forms.ModelForm):
    class Meta:
        model = Teste
        fields = ('titulo', 'capa_tcc', 'autores', 'orientador', 'status', 'data_entrega')