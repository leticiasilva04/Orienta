from django.urls import path
from . import views

#Essas são as rotas da tela home do tcc
urlpatterns = [
    path('<int:tcc_id>/', views.tcc_home, name='tcc_home'),  
    path('<int:tcc_id>/editar/', views.editar_tcc, name='editar_tcc'),
    path('<int:tcc_id>/deletar/', views.deletar_tcc, name='deletar_tcc'),
   #arrumar dps com o Carlinhos, pra seguir esse estilo path('<int:tcc_id>/chat/', views.chat_tcc, name='chat_tcc'), 
]
