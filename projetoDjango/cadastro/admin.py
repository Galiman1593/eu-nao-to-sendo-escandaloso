from django.contrib import admin
from .models import Curso, Turma
from .models import Alunos
from .models import Professores
# Register your models here.
admin.site.register(Curso)
admin.site.register(Alunos)
admin.site.register(Professores)
admin.site.register(Turma)
