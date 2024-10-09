from django.shortcuts import render, redirect
from .forms import TCCForm
from django.contrib.auth.decorators import login_required

@login_required
def criar_tcc(request):
    if request.method == 'POST':
        form = TCCForm(request.POST, request.FILES)
        if form.is_valid():
            tcc = form.save(commit=False)
            tcc.orientador = request.user
            tcc.status = 'ativo'
            tcc.save()
            form.save_m2m()
            return redirect('home_chat')
    else:
        form = TCCForm()
    return render(request, 'criar_tcc.html', {'form': form})

