# forms/views.py

from django.shortcuts import render, redirect
from .forms import TCCForm  # Corrigido para o caminho certo
from django.contrib.auth.decorators import login_required

@login_required
def criar_tcc(request):
    if request.method == 'POST':
        form = TCCForm(request.POST, request.FILES)
        if form.is_valid():
            tcc = form.save(commit=False)
            tcc.orientador = request.user  # Define o orientador como o usuário logado
            tcc.status = 'ativo'  # Define o status como ativo
            tcc.save()
            form.save_m2m()  # Salva a relação de muitos-para-muitos
            return redirect('home_chat')  # Redireciona para a página inicial ou outra que você preferir
    else:
        form = TCCForm()
    return render(request, 'criar_tcc.html', {'form': form})  # Use apenas o nome do template

