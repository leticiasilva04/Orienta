from django.shortcuts import render, get_object_or_404
from .models import TCC
from django.shortcuts import redirect
from .forms import TCCForm 


def tcc_home(request, tcc_id):
    tcc = get_object_or_404(TCC, id=tcc_id)
    return render(request, 'tcc_home.html', {'tcc': tcc})

def editar_tcc(request, tcc_id):
    tcc = get_object_or_404(TCC, id=tcc_id)

    if request.method == 'POST':
        form = TCCForm(request.POST, request.FILES, instance=tcc)
        if form.is_valid():
            form.save()
            return redirect('tcc_home', tcc_id=tcc.id)
    else:
        form = TCCForm(instance=tcc)

    return render(request, 'tcc_edit.html', {'form': form, 'tcc': tcc})

def deletar_tcc(request, tcc_id):
    tcc = get_object_or_404(TCC, id=tcc_id)
    
    if request.method == 'POST':
        tcc.delete()
        return redirect('home')  #Dps de excluir, tem que ir pra tela inicial
    
    return render(request, 'deletar_tcc.html', {'tcc': tcc})
