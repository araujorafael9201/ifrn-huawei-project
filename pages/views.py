from django.shortcuts import render

from .models import Aluno

# EVENTOS
def ict_job_fair_brasil(request):
    return render(request, 'pages/ict-job-fair-brasil.html')

def ict_competition_brasil(request):
    return render(request, 'pages/ict-competition-brasil.html')

def seeds_for_the_future(request):
    return render(request, 'pages/seeds-for-the-future.html')



def index(request):
    return render(request, 'pages/index.html')

def sobre_ict_academy(request):
    return render(request, 'pages/sobre_ict_academy.html')

def sobre_huawei(request):
    return render(request, 'pages/sobre_huawei.html')

def cloud_service(request):
    return render(request, 'pages/cloud_service.html')

def inteligencia_artificial(request):
    return render(request, 'pages/inteligencia_artificial.html')

def datacom(request):
    return render(request, 'pages/datacom.html')

def cincog(request):
    return render(request, 'pages/5g.html')
    
def instrutores(request):
    return render(request, 'pages/instrutores.html')

def certificacao(request):
    return render(request, 'pages/certificacao.html')

def contato(request):
    return render(request, 'pages/contato.html')

def laboratorios(request):
    return render(request, 'pages/laboratorios.html')

def inscricao(request):
    return render(request, 'pages/inscricao.html')

def cadastro(request):
    return render(request, 'pages/cadastro.html')

def cadastrar(request):
    if request.method == 'POST':    
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        email = request.POST['email']
        genero = request.POST['genero']
        formacao = request.POST['formacao']
        nascimento = request.POST['nascimento']
        aluno_ifrn = request.POST['aluno-ifrn']
        servidor_ifrn = request.POST['servidor-ifrn']
        instituicao_de_ensino = request.POST['instituicao-de-ensino']
        email = request.POST['email']
        celular = request.POST['celular']
        senha = request.POST['senha']
        comprovante_conhecimento = request.POST['comprovante-conhecimento']

        if int(genero) == 1:
            genero = 'M'
        else:
            genero = 'F'
        
        formacoes = ['Fundamental I Imcompleto', 'Fundamental I Completo', 'Fundamental II Inconpleto', 'Fundamental II Completo', 'Ensino Médio Imcompleto', 'Ensino Médio Completo', 'Ensino Superior Imcompleto', 'Ensino Superior Completo', 'Pós-Graduação']
        formacao = formacoes[int(formacao) - 1]

        if int(aluno_ifrn) == 1:
            aluno_ifrn = False
        else:
            aluno_ifrn = True

        if int(servidor_ifrn) == 1:
            servidor_ifrn = False
        else:
            servidor_ifrn = True

        aluno = Aluno(cpf=cpf, nome=nome, genero=genero, formacao=formacao, nascimento=nascimento, aluno_ifrn=aluno_ifrn, servidor_ifrn=servidor_ifrn, instituicao_de_ensino=instituicao_de_ensino, email=email, celular=celular, senha=senha)
        
        aluno.save()

        return render(request, 'pages/index.html')
def login(request):
    return render(request, 'pages/login.html')

