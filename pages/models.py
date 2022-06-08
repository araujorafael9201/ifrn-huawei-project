from django.db import models

class Turma(models.Model):
    curso = models.CharField(max_length=30)

class Aluno(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=255)
    genero = models.CharField(max_length=9)
    formacao = models.CharField(max_length=255)
    nascimento = models.DateField()
    aluno_do_ifrn = models.BooleanField()
    servidor_do_ifrn = models.BooleanField()

    email = models.EmailField()
    celular = models.CharField(max_length=11)

    # Senha ainda está como texto simples
    senha = models.CharField(max_length=255)

    turmas = models.ForeignKey(Turma, on_delete=models.DO_NOTHING)
    comprovacao_conhecimento = models.FileField(upload_to=f'pdfs/user_{0}'.format(cpf))

class Professor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    # Senha ainda está como texto simples
    senha = models.CharField(max_length=255)
    turma = models.OneToOneField(Turma, on_delete=models.SET_DEFAULT, default='Sem Professor')
