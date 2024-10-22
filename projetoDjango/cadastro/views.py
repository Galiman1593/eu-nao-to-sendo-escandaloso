from django.shortcuts import redirect, render
from django.http import HttpResponse

from cadastro.forms import AlunoForm, CursoForm, ProfForm, TurmaForm
from .models import Curso, Alunos, Professores, Turma
from django.contrib import messages

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
            try:
                form.save()
                messages.info(request, "Novo curso cadastrado")
            except:
                messages.error(request, "Não foi possivel cadastrar")    
            return redirect('listarcursos')
    form = CursoForm()
    return render(request, "form_curso.html", {'formulario':form}) 

def alterarcurso(request, codigo):
    c = Curso.objects.get(id=codigo)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=c)
        if form.is_valid():
            try:
                form.save()
                messages.info(request, "Alterado com sucesso.")
            except:
                messages.error(request, "Não foi possivel alterar")    
            return redirect('listarcursos')
   
    form = CursoForm(instance=c)
    return render(request, 'form_curso.html', {'formulario': form})

def excluircurso(request, codigo):
    c = Curso.objects.get(id=codigo)
    try:
        c.delete()
        messages.info(request, "Excluído com sucesso.")
    except:
        messages.error(request, "Não é possível excluir.")
    return redirect('listarcursos')

#alunos
def listaralunos(request):
    alunos = Alunos.objects.order_by('nome')
    return render(request, 'listaralunos.html', {'alunos': alunos})

def incluiralunos(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            try:
                form.save() 
                messages.info(request, "Novo aluno cadastrado")
            except:
                messages.error(request, "Não foi possivel cadastrar")    
            return redirect('listaralunos')
    form = AlunoForm()
    return render(request, "form_aluno.html", {'formulario':form})   

def alteraralunos(request, codigo):
    a = Alunos.objects.get(id=codigo)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=a)
        if form.is_valid():
            try:
                form.save()
                messages.info(request, "Alterado com sucesso.")
            except:
                messages.error(request, "Não foi possivel alterar")
            return redirect('listaralunos')
   
    form = AlunoForm(instance=a)
    return render(request, 'form_Aluno.html', {'formulario': form})

def excluiralunos(request, codigo):
    a = Alunos.objects.get(id=codigo)
    try:
        a.delete()
        messages.info(request, "excluido com sucesso")
    except:
        messages.error(request, "Não foi possivel excluir")    
    return redirect('listaralunos')


#turmas

def listarturmas(request):
    turmas = Turma.objects.order_by('dataInicio')
    return render(request, 'listarturmas.html', {'turmas': turmas})

def incluirturma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            try:
                form.save() 
                messages.info(request, "Nova turma cadastrado")
            except:
                messages.error(request, "Não foi possivel cadastrar")
            return redirect('listarturmas')
    form = TurmaForm()
    return render(request, 'form_turma.html', {'formulario': form})

def alterarturma(request, codigo):
    t = Turma.objects.get(id=codigo)
    if request.method == 'POST':
        form = TurmaForm(request.POST, instance=t)
        if form.is_valid():
            try:
                form.save()
                messages.info(request, "Alterado com sucesso.")
            except:
                messages.error(request, "Não foi possivel alterar")
            return redirect('listarturmas')

    form = TurmaForm(instance=t)
    return render(request, 'form_turma.html', {'formulario': form})

def excluirturma(request, codigo):
    t = Turma.objects.get(id=codigo)
    try:
        t.delete()
        messages.info(request, "Excluido com sucesso")
    except:
        messages.error(request, "Não foi possivel excluir")    
    return redirect('listarturmas')


    

#Professores
def listarprofessores(request):
    professores = Professores.objects.order_by('nome')
    return render(request, 'listarprofessores.html', {'Professores': professores})

def incluirprofessor(request):
    if request.method == 'POST':
        form = ProfForm(request.POST)
        if form.is_valid():
            try:
                form.save() 
                messages.info(request, "Novo professor cadastrado")
            except:
                messages.error(request, "Não foi possivel cadastrar")
            return redirect('listarprofessores')
    form = ProfForm()
    return render(request, "form_professor.html", {'formulario':form}) 

def alterarprofessor(request, codigo):
    p = Professores.objects.get(id=codigo)
    if request.method == 'POST':
        form = ProfForm(request.POST, instance=p)
        if form.is_valid():
            try:
                form.save()
                messages.info(request, "Alterado com sucesso.")
            except:
                messages.error(request, "Não foi possivel alterar")
            return redirect('listarprofessores')
   
    form = ProfForm(instance=p)
    return render(request, 'form_professor.html', {'formulario': form})

def excluirprofessor(request, codigo):
    p = Professores.objects.get(id=codigo)
    try:
        p.delete()
        messages.info(request, "Excluido com sucesso")
    except:
        messages.error(request, "Não foi possivel esxcluir")    
    return redirect('listarprofessores')

