from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('segundo', views.segundo, name='segundo'),
    path('pagina', views.pagina, name='pagina'),
    path('mensagem', views.mensagem, name='mensagem'),

    #cursos
    path('listarcursos', views.listarcursos, name='listarcursos'),
    path('incluircursos', views.incluircursos, name='incluircurso'),
    path('alterarcurso/<int:codigo>', views.alterarcurso, name='alterarcurso'),

    #alunos
    path('listaralunos', views.listaralunos, name='listaralunos'),
    path('incluiraluno', views.incluiralunos, name='incluiralunos'),
    
    #professores
    path('listarprofessores', views.listarprofessores, name='listarprofessores'),
    path('incluirprofessor', views.incluirprofessor, name='incluirprofessor'),
]



