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
    path('excluircurso/<int:codigo>', views.excluircurso, name='excluircurso'),

    #alunos
    path('listaralunos', views.listaralunos, name='listaralunos'),
    path('incluiraluno', views.incluiralunos, name='incluiralunos'),
    path('alteraralunos/<int:codigo>', views.alteraralunos, name='alteraralunos'),
    path('excluiralunos/<int:codigo>', views.excluiralunos, name='excluiralunos'),
    
    #professores
    path('listarprofessores', views.listarprofessores, name='listarprofessores'),
    path('incluirprofessor', views.incluirprofessor, name='incluirprofessor'),
    path('alterarprofessor/<int:codigo>', views.alterarprofessor, name='alterarprofessor'),
     path('excluirprofessor/<int:codigo>', views.excluirprofessor, name='excluirprofessor'),

    #turmas
    path('listarturmas', views.listarturmas, name='listarturmas'),
    path('incluirturma', views.incluirturma, name='incluirturma'),
    path('alterarturma/<int:codigo>', views.alterarturma, name='alterarturma'),
    path('excluirturma/<int:codigo>', views.excluirturma, name='excluirturma'),
]



