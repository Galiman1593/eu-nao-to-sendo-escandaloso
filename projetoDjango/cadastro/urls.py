from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('segundo', views.segundo, name='segundo'),
    path('pagina', views.pagina, name='pagina'),
    path('mensagem', views.mensagem, name='mensagem'),

    #cursos
    path('listarcursos', views.listarcursos, name='listarcursos'),

    #alunos
    path('listaralunos', views.listaralunos, name='listaralunos'),
    
    #professores
    path('listarprofessores', views.listarprofessores, name='listarprofessores'),
]



