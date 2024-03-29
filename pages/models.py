from django.db import models
import os


class Aluno(models.Model):
    username = models.CharField(max_length=255, default="")
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, default="")
    data_inscricao = models.DateField(null=True)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    # turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True)

    senha = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome


class Turma(models.Model):
    nome_do_curso = models.CharField(max_length=255, default='Curso')
    professor = models.ForeignKey(Professor, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome_do_curso

def caminho_documento(instance, filename):
    nome, extensao = os.path.splitext(filename)
    return f'./uploads/{instance.aluno.cpf}-{instance.turma.nome_do_curso}{extensao}'

class Inscricao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

class Nota(models.Model):
    valor = models.IntegerField(default=6)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

class Falta(models.Model):
    quantidade = models.IntegerField(default=0)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

class Aula(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data = models.DateTimeField()
    desc = models.TextField(max_length=255)
    
