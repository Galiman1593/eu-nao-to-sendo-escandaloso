from django.forms import ModelForm
from cadastro.models import Alunos, Curso, Professores

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class AlunoForm(ModelForm):
    class Meta:
        model = Alunos
        fields = '__all__'

class ProfForm(ModelForm):
    class Meta:
        model = Professores
        fields = '__all__'       
                
        
