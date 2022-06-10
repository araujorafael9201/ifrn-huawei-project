from django.db import models

class Turma(models.Model):
    nome_do_curso = models.CharField(max_length=255, default='Curso')

class Aluno(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=255)
    genero = models.CharField(max_length=9)
    formacao = models.CharField(max_length=255)
    nascimento = models.DateField()
    aluno_ifrn = models.BooleanField()
    servidor_ifrn = models.BooleanField()
    instituicao_de_ensino = models.CharField(max_length=255, default=' ')

    email = models.EmailField(default='desconhecido@email.com')
    celular = models.CharField(max_length=11)

    # Senha ainda está como texto simples
    senha = models.CharField(max_length=255)

class Professor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True)

    # Senha ainda está como texto simples
    senha = models.CharField(max_length=255)


class Inscricao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    aprovada = models.BooleanField(default=False)
    documento = models.FileField(upload_to='./uploads')

