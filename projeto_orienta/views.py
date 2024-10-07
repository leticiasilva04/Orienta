from django.shortcuts import render, redirect
from app_tcc.models import TCC
from app_tcc.models import Teste
from django.contrib.auth.models import User
from app_tcc.forms import TesteForm


def orientador(request):
    tasks = Teste.objects.all()  # Fetch all tasks
    context = {'tasks': tasks}  # Create a context dictionary
    return render(request, 'orientador.html', context)  # Render the template


def teste_view(request):
    if request.method == 'POST':
        form = TesteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teste_success')  # redirect to a success page
    else:
        form = TesteForm()
    return render(request, 'teste.html', {'form': form})
 
def teste_success(request):    
    return render(request, 'teste_success.html')

def index(request):
    return render(request, 'index.html')
