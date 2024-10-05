from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso, Alunos, Professores

# Create your views here.
def index(request):
    return render(request, 'inicio.html')

def segundo(request):
    return HttpResponse("<h1>Segunda</h1>")

def pagina(request):
    return render(request, 'pagina.html')

def mensagem(request):
    return render(request, 'inicio.html')

#Cursos
def listarcursos(request):
    cursos = Curso.objects.order_by('nome')
    return render(request, 'listarcursos.html', {'cursos': cursos})

#alunos
def listaralunos(request):
    alunos = Alunos.objects.order_by('nome')
    return render(request, 'listaralunos.html', {'alunos': alunos})

#Professores
def listarprofessores(request):
    professores = Professores.objects.order_by('nome')
    return render(request, 'listarprofessores.html', {'Professores': professores})
