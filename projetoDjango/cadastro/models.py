from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.nome


class Alunos(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.nome


class Professores(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    matricula = models.CharField(max_length=5)

    def __str__(self):
        return self.nome