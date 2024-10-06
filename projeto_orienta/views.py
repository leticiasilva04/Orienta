from django.shortcuts import render
from app_tcc.models import TCC

def orientador(request):
    tasks = TCC.objects.all()  # Fetch all tasks
    context = {'tasks': tasks}  # Create a context dictionary
    return render(request, 'orientador.html', context)  # Render the template