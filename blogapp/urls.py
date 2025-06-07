from django.urls import path
from . import views 


urlpatterns = [
    path('home/', views.home, name='home'), 
    path('home/artigo/<int:artigo_id>/', views.artigo, name='artigo'), 
    path('home/login/configuracoes/', views.configuracoes, name='configuracoes'), 
    path('home/login/adicionar/', views.adicionar, name='adicionar'), 
    path('home/login/editar/<int:artigo_id>', views.editar, name='editar'), 
    path('home/login/deletar/<int:artigo_id>', views.deletar, name='deletar'), 
    path('home/login/', views.login, name='login'), 
]