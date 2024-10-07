# forms/urls.py

from django.urls import path
from .views import criar_tcc

urlpatterns = [
    path('criar_tcc/', criar_tcc, name='criar_tcc'),  # Corrigido para que o caminho esteja certo
]
