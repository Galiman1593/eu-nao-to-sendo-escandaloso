from django.shortcuts import redirect, render
from django.http import HttpResponse

from cadastro.forms import CursoForm
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

def incluircursos(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarcursos')
    form = CursoForm()
    return render(request, "form_curso.html", {'formulario':form})    

#alunos
def listaralunos(request):
    alunos = Alunos.objects.order_by('nome')
    return render(request, 'listaralunos.html', {'alunos': alunos})

#Professores
def listarprofessores(request):
    professores = Professores.objects.order_by('nome')
    return render(request, 'listarprofessores.html', {'Professores': professores})
