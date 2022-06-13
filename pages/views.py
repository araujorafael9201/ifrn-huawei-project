from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email


from .models import Aluno, Inscricao, Turma

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


##
def inscricao(request):
    try:
        cursos = Turma.objects.all()

        return render(request, 'pages/inscricao.html', {'aluno_id': request.session['aluno_id'], 'cursos': cursos})
    except KeyError:
        messages.error(request, 'Para se inscrever, você deve está logado.')
        return render(request, 'pages/login.html')

def inscrever(request):
    if request.method == 'POST':
        curso = Turma.objects.all().filter(pk=request.POST['curso'])[0]
        documento = request.FILES['comprovante-conhecimento']

        aluno = Aluno.objects.all().filter(pk=request.session['aluno_id'])[0]

        # Documento ainda não funciona (salva só o nome)
        inscricao = Inscricao(turma=curso, documento=documento, aluno=aluno)
        inscricao.save()

        messages.success(request, 'Inscrição realizada com sucesso!')
        return redirect('index')

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

        if not nome or not nascimento or not email or not celular or not senha:
            messages.error(request, 'Você deve preencher todos os campos.')
            return render(request, 'pages/cadastro.html')
        
        if aluno_ifrn == False and servidor_ifrn == False:
            if not instituicao_de_ensino:
                messages.error(request, 'Você deve preencher todos os campos.')
                return render(request, 'pages/cadastro.html')
        
        try:
            validate_email(email)
        except:
            messages.error(request, 'E-mail inválido.')
            return render(request, 'pages/cadastro.html')

        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado.')
            return render(request, 'pages/cadastro.html')

        if len(senha) < 8:
            messages.error(request, 'A senha deve conter pelo menos 8 caracteres.')
            return render(request, 'pages/cadastro.html')
        
        messages.success(request, 'Cadastrado com sucesso!')

        aluno = Aluno(cpf=cpf, nome=nome, genero=genero, formacao=formacao, nascimento=nascimento, aluno_ifrn=aluno_ifrn, servidor_ifrn=servidor_ifrn, instituicao_de_ensino=instituicao_de_ensino, email=email, celular=celular, senha=senha)
        aluno.save()

        return redirect('login')


def login(request):
    if 'aluno_id' in request.session:
        messages.warning(request, 'Você já está logado!')
        return render(request, 'pages/index.html')
    else:
        return render(request, 'pages/login.html')

def logar(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['pwd']

        try:
            aluno = Aluno.objects.all().filter(email=email, senha=senha)[0]
            request.session['aluno_id'] = aluno.id
            return redirect('/')
        except:
            messages.error(request, 'Email ou senha inválidos.')
            return render(request, 'pages/login.html')

def deslogar(request):
    try:
        del request.session['aluno_id']
        return redirect('/')
    except:
        messages.error(request, 'Você não está logado.')
        return render(request, 'pages/index.html')