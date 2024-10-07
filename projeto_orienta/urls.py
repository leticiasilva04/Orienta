"""
URL configuration for projeto_orienta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
<<<<<<< HEAD
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from projeto_orienta.views import orientador
#from projeto_orienta.views import teste
from projeto_orienta.views import index
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('index/', index, name='index_page'),
    #path('teste/', teste, name='teste'),  
    path('orientador/', views.orientador, name='orientador'),
    path('teste/', views.teste_view, name='teste'),
    path('teste_success', views.teste_success, name='teste_success'),  # create a success page

=======
from django.urls import path, include
from chat import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_chat, name='home_chat'),    
    path('chat/<str:room_name>/', views.room, name='sala1'), 
    path('', views.home_chat, name='home_chat'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('forms/', include('forms.urls')),  # Incluindo as URLs da pasta forms
    path('accounts/', include('django.contrib.auth.urls')), 
     path('logout/', LogoutView.as_view(next_page='/admin/login/?next=/admin/app_tcc/user/'), name='logout'),
>>>>>>> d58ab90a25e685ff52cb2abb33445af036ba18a0
]

