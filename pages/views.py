from http.client import HTTPResponse
from lib2to3.pytree import convert
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from .validador.valida_cpf import validar_cpf
from django.contrib.auth.hashers import make_password, check_password


from .models import Aluno, Inscricao, Turma, Professor, Nota


def index(request):
    return render(request, 'pages/index.html')

def contato(request):
    return render(request, 'pages/contact.html')

def certificacao(request):
    return render(request, 'pages/certification.html')

def instrutores(request):
    return render(request, 'pages/instructors.html')

def laboratorios(request):
    return render(request, 'pages/laboratories.html')



def sobre_ict_academy(request):
    return render(request, 'pages/sobre/ict-academy.html')

def sobre_huawei(request):
    return render(request, 'pages/sobre/huawei.html')



def cloud_service(request):
    return render(request, 'pages/cursos/cloud-service.html')

def inteligencia_artificial(request):
    return render(request, 'pages/cursos/artificial-intelligence.html')

def datacom(request):
    return render(request, 'pages/cursos/datacom.html')

def cincog(request):
    return render(request, 'pages/cursos/5g-networks.html')

def hands_on(request):
    return render(request, 'pages/hands-on.html')



def ict_job_fair_brasil(request):
    return render(request, 'pages/eventos/ict-job-fair-brasil.html')


def ict_competition_brasil(request):
    return render(request, 'pages/eventos/ict-competition-brasil.html')


def seeds_for_the_future(request):
    return render(request, 'pages/eventos/seeds-for-the-future.html')




##
def inscricao(request):
    try:
        cursos = Turma.objects.all()

        return render(request, 'pages/inscricao.html', {'aluno_id': request.session['aluno_id'], 'cursos': cursos})
    except KeyError:
        messages.error(request, 'Para se inscrever, você deve está logado.')
        return redirect('/login')


def inscrever(request):
    if request.method == 'POST':
        curso = Turma.objects.get(pk=request.POST['curso'])
        documento = request.FILES['comprovante-conhecimento']

        aluno = Aluno.objects.get(pk=request.session['aluno_id'])

        inscricao = Inscricao(turma=curso, documento=documento, aluno=aluno)
        inscricao.save()

        messages.success(request, 'Inscrição realizada com sucesso!')
        return redirect('index')

def desinscrever(request):
    if request.method == 'POST':
        inscricao = Inscricao.objects.get(pk=request.POST['inscricao'])

        inscricao.delete()
        messages.success(request, 'Inscrição Cancelada com Sucesso!')
        return redirect('/aluno')

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

        # SENHA
        senha = make_password(senha)

        if int(genero) == 1:
            genero = 'M'
        else:
            genero = 'F'

        formacoes = ['Fundamental I Incompleto', 'Fundamental I Completo', 'Fundamental II Incompleto', 'Fundamental II Completo',
                     'Ensino Médio Incompleto', 'Ensino Médio Completo', 'Ensino Superior Incompleto', 'Ensino Superior Completo', 'Pós-Graduação']
        formacao = formacoes[int(formacao) - 1]

        if int(aluno_ifrn) == 1:
            aluno_ifrn = False
        else:
            aluno_ifrn = True

        if int(servidor_ifrn) == 1:
            servidor_ifrn = False
        else:
            servidor_ifrn = True

        #
        # EXEÇÕES: CAMPOS NÃO PREENCHIDOS
        #
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

        #
        # EXEÇÕES: JÁ CADASTRADO NO SISTEMA
        #

        if Aluno.objects.filter(cpf=cpf).exists():
            messages.error(request, 'CPF já cadastrado.')
            return render(request, 'pages/cadastro.html')

        if Aluno.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado.')
            return render(request, 'pages/cadastro.html')

        if Aluno.objects.filter(celular=celular).exists():
            messages.error(request, 'Número de celular já cadastrado.')
            return render(request, 'pages/cadastro.html')

        #
        # EXEÇÕES: TAMANHO DAS ENTRADAS
        #
        if len(senha) < 8:
            messages.error(
                request, 'A senha deve conter pelo menos 8 caracteres.')
            return render(request, 'pages/cadastro.html')

        if len(celular) > 11:
            messages.error(request, 'Número de celular inválido.')
            return render(request, 'pages/cadastro.html')

        nasc = nascimento.split('-')
        ano_nasci = int(nasc[0])

        if ano_nasci > 2022 or ano_nasci < 1950:
            messages.error(request, 'Data de nascimento inválida.')
            return render(request, 'pages/cadastro.html')

        vl_cpf = validar_cpf(cpf)
        if not vl_cpf:
            messages.error(request, 'CPF inválido.')
            return render(request, 'pages/cadastro.html')

        messages.success(request, 'Cadastrado com sucesso!')

        aluno = Aluno(cpf=cpf, nome=nome, genero=genero, formacao=formacao, nascimento=nascimento, aluno_ifrn=aluno_ifrn,
                      servidor_ifrn=servidor_ifrn, instituicao_de_ensino=instituicao_de_ensino, email=email, celular=celular, senha=senha)

        aluno.save()

        return redirect('login')

def login(request):
    if 'prof_id' in request.session:
        messages.warning(request, 'Você não pode fazer login como Aluno e Professor Simultaneamente!')
        return redirect('/')

    elif 'aluno_id' in request.session:
        messages.warning(request, 'Você já está logado!')
        return redirect('/')
    else:
        return render(request, 'pages/login.html')


def logar(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['pwd']

        try:
            aluno = Aluno.objects.all().filter(email=email)[0]
            if check_password(senha, aluno.senha):
                request.session['aluno_id'] = aluno.id
                return redirect('/')
            else:
                raise Exception
        except:
            messages.error(request, 'Email ou senha inválidos.')
            return redirect('/login')


def deslogar(request):
    try:
        del request.session['aluno_id']
        return redirect('/')
    except:
        try:
            del request.session['prof_id']
            return redirect('/')
        except:
            messages.error(request, 'Você não está logado.')
            return redirect('/')

def professor_login(request):
    if 'aluno_id' in request.session:
        messages.warning(request, 'Você não pode fazer login como Aluno e Professor Simultaneamente!')
        return redirect('/')
    elif 'prof_id' in request.session:
        messages.warning(request, 'Você já está logado!')
        return redirect('/professor')
    else:
        return render(request, 'pages/loginprof.html')

def professor_logar(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['pwd']

        try:
            professor = Professor.objects.filter(email=email, senha=senha)[0]
            request.session['prof_id'] = professor.id
            return redirect('/professor')
        except:
            messages.error(request, 'Email ou senha inválidos.')
            return redirect('/proflogin')

def professor(request):
    try:
        prof = Professor.objects.select_related('turma').get(pk=request.session['prof_id'])
        turma = prof.turma

        inscricoes = Inscricao.objects.select_related('aluno').all().filter(turma=turma)

        aprovados, pendentes = [], []

        notas_faltando = False
        for i in inscricoes:
            if i.aprovada:
                n = Nota.objects.filter(aluno=i.aluno.id, turma=i.turma.id)
                if n:
                    aluno_final = {'inscricao': i, 'nota': n[0]}
                    aprovados.append(aluno_final)
                else:
                    notas_faltando = True
                    aprovados.append({'inscricao': i, 'nota': None})
            else:
                pendentes.append(i)

        return render(request, 'pages/professor.html', {'aprovados': aprovados, 'pendentes': pendentes, 'turma': turma, 'professor': prof, 'notas': notas, 'notas_faltando': notas_faltando})
    except KeyError:
        messages.error(request, 'Por favor, Faça Login!')
        return redirect('/proflogin')

def aluno(request):
    inscricoes = Inscricao.objects.all().filter(aluno=request.session['aluno_id'])

    info = []

    for i in inscricoes:
        nota = Nota.objects.filter(aluno=request.session['aluno_id'], turma = i.turma)
        if nota:
            info.append({'inscricao': i, 'nota': nota[0]})
        else:
            info.append({'inscricao': i})

    try:
        return render(request, 'pages/aluno.html', {'aluno_id': request.session['aluno_id'], 'info': info})
    except KeyError:
        messages.error(request, 'Por favor, Faça Login!')
        return redirect('/login')

def turmainfo(request, id):
    turma = Turma.objects.get(pk=id)

    # Pegar alunos da Turma
    alunos = []
    for i in Inscricao.objects.select_related('aluno').filter(turma = turma.id):
        if i.aprovada:
            alunos.append(i.aluno)
            
    # Pegar Informações do Professor
    professor = Professor.objects.get(turma=turma.id)

    return render(request, 'pages/turmainfo.html', {'turma': turma, 'alunos': alunos, 'professor': professor})



def matricula(request):
    if request.method == 'POST':
        for value in request.POST:
            if value not in ['csrfmiddlewaretoken', 'turma_id']:
                insc = Inscricao.objects.get(pk=value)
                insc.aprovada = True
                insc.save()         

        return redirect('/professor')

def notas(request):
    if request.method=='POST':
        turma = Professor.objects.select_related('turma').get(pk=request.POST['idprof']).turma
        alunos = [a for a in request.POST if a not in ['csrfmiddlewaretoken', 'idprof']]

        for aluno in alunos:
            if request.POST[aluno] != '':
                al = Aluno.objects.get(pk=aluno)
                nota = Nota(valor=request.POST[aluno], aluno=al, turma=turma)
                nota.save()

        messages.success(request, 'Notas Adicionadas com Sucesso!')
        return redirect('professor')

def docs(request, docname):
    # sei fazer n :(
    return

def suporte(request):
    return render(request, 'pages/suporte.html')