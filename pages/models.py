from django.db import models

# Create your models here.

class Aluno(models.Model):
    cpf = models.CharField(max_length=10)
    nome = models.CharField(max_length=50)
    genero = models.CharField(max_length=10)
    formacao = models.CharField(max_length=20)
    nascimento = models.DateField()
    aluno_do_ifrn = models.BooleanField()
    servidor_do_ifrn = models.BooleanField()

    email = models.EmailField()
    celular = models.CharField(max_length=15)

    # Senha ainda está como texto simples
    senha = models.CharField(max_length=20)

    turmas = models.ForeignKey('Turma', on_delete=models.CASCADE)
    
    # Faltando arquivo de comprovação de conhecimento
    #comprovacao_conhecimento = models.FileField() ?

class Turma(models.Model):
    curso = models.CharField(max_length=30)
    # estado dos alunos?

class Professor(models.Model):
    nome = models.CharField(max_length=50)
    # Senha ainda está como texto simples
    senha = models.CharField(max_length=20)
    turma = models.OneToOneField('Turma', on_delete=models.SET_DEFAULT, default='Sem Professor')
