from http.client import HTTPResponse
from lib2to3.pytree import convert
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from .validador.valida_cpf import validar_cpf
from django.contrib.auth.hashers import make_password, check_password
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
import pandas
from datetime import date

from .models import Aluno, Inscricao, Turma, Professor, Nota, Falta, Aula


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
# def inscricao(request):
#     try:
#         cursos = Turma.objects.all()

#         return render(request, 'pages/inscricao.html', {'aluno_id': request.session['aluno_id'], 'cursos': cursos})
#     except KeyError:
#         messages.error(request, 'Para se inscrever, você deve está logado.')
#         return redirect('/login')


# def inscrever(request):
#     if request.method == 'POST':
#         curso = Turma.objects.get(pk=request.POST['curso'])
#         documento = request.FILES['comprovante-conhecimento']

#         aluno = Aluno.objects.get(pk=request.session['aluno_id'])

#         insc_check = Inscricao.objects.all().filter(turma=curso, aluno=aluno)

#         if not insc_check:
#             inscricao = Inscricao(turma=curso, documento=documento, aluno=aluno)
#             inscricao.save()

#             messages.success(request, 'Inscrição realizada com sucesso!')
#         else:
#             messages.error(request, 'Você já realizou sua inscrição nesse curso!')

#         return redirect('index')

# def desinscrever(request):
#     if request.method == 'POST':
#         inscricao = Inscricao.objects.get(pk=request.POST['inscricao'])

#         inscricao.delete()
#         messages.success(request, 'Inscrição Cancelada com Sucesso!')
#         return redirect('/aluno')

# def cadastro(request):
#     return render(request, 'pages/cadastro.html')


# def login(request):
#     if 'prof_id' in request.session:
#         messages.warning(request, 'Você não pode fazer login como Aluno e Professor Simultaneamente!')
#         return redirect('/')

#     elif 'aluno_id' in request.session:
#         messages.warning(request, 'Você já está logado!')
#         return redirect('/')
#     else:
#         return render(request, 'pages/login.html')


# def logar(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         senha = request.POST['pwd']

#         try:
#             aluno = Aluno.objects.all().filter(email=email)[0]
#             if check_password(senha, aluno.senha):
#                 request.session['aluno_id'] = aluno.id
#                 return redirect('/')
#             else:
#                 raise Exception
#         except:
#             messages.error(request, 'Email ou senha inválidos.')
#             return redirect('/login')


def deslogar(request):
        try:
            del request.session['prof_id']
            return redirect('/')
        except:
            messages.error(request, 'Você não está logado.')
            return redirect('/')

def professor_login(request):
    if 'prof_id' in request.session:
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
        prof = Professor.objects.get(pk=request.session['prof_id'])
        turmas = Turma.objects.all().filter(professor=prof)

        return render(request, 'pages/profinicio.html', {'turmas':turmas})

    except KeyError:
        messages.error(request, 'Por favor, Faça Login!')
        return redirect('/proflogin')

def professorturma(request, turmaid):
        inscricoes = Inscricao.objects.select_related('aluno').all().filter(turma=turmaid)
        turma = Turma.objects.select_related('professor').get(id=turmaid)
        prof = Professor.objects.get(pk=request.session['prof_id'])
        insc = []

        if turma.professor.id != request.session['prof_id']:
            messages.error(request, 'Você não tem permissão para acessar esta página!')
            return render(request, 'pages/index.html')


        else:
            notas_faltando = False
            for i in inscricoes:
                    n = Nota.objects.filter(aluno=i.aluno.id, turma=i.turma.id)
                    faltas = Falta.objects.filter(aluno=i.aluno.id, turma=i.turma.id)
                    if n:
                        if faltas:
                            aluno_final = {'inscricao': i, 'nota': n[0], 'faltas': faltas[0].quantidade}
                            insc.append(aluno_final)
                        else:
                            aluno_final = {'inscricao': i, 'nota': n[0], 'faltas': 0}
                            insc.append(aluno_final)

                    else:
                        if faltas:
                            notas_faltando = True
                            insc.append({'inscricao': i, 'nota': None, 'faltas': faltas[0].quantidade})
                        else:
                            notas_faltando = True
                            insc.append({'inscricao': i, 'nota': None, 'faltas': 0})
            return render(request, 'pages/professor.html', {'inscricoes': insc,'turma': turma, 'professor': prof, 'notas': notas, 'notas_faltando': notas_faltando})

def aluno(request):
    if request.method == 'POST':
        try:
            aluno = Aluno.objects.get(username=request.POST['username'])
            inscricoes = Inscricao.objects.all().filter(aluno=aluno.id)

            info = []

            for i in inscricoes:
                nota = Nota.objects.filter(aluno=aluno.id, turma=i.turma).first()
                faltas = Falta.objects.filter(aluno=aluno.id, turma=i.turma).first()
                if nota:
                    if faltas:
                        info.append({'inscricao': i, 'nota': nota, 'faltas': faltas.quantidade})
                    else:
                        info.append({'inscricao': i, 'nota': nota})
                        
                else:
                    if faltas:
                        info.append({'inscricao': i, 'faltas': faltas.quantidade})
                    else:
                        info.append({'inscricao': i})

            return render(request, 'pages/aluno.html', {'aluno_id': aluno.id, 'info': info})
        except:
            messages.error(request, 'Aluno não encontrado!')
            return redirect('/aluno')
    else:
        return render(request, 'pages/login.html')

def turmainfo(request, id):
    turma = Turma.objects.get(pk=id)

    # Pegar alunos da Turma
    alunos = []
    for i in Inscricao.objects.select_related('aluno').filter(turma = turma.id):
        alunos.append(i.aluno)
            
    # Pegar Informações do Professor
    professor = Professor.objects.get(turma=turma.id)

    return render(request, 'pages/turmainfo.html', {'turma': turma, 'alunos': alunos, 'professor': professor})

def notas(request, turmaid):
    if request.method=='POST':
        turma = Turma.objects.get(id=turmaid)
        alunos = [a for a in request.POST if a not in ['csrfmiddlewaretoken', 'idprof']]

        for aluno in alunos:
            if request.POST[aluno] != '':
                al = Aluno.objects.get(pk=aluno)
                nota = Nota(valor=request.POST[aluno], aluno=al, turma=turma)
                nota.save()

        messages.success(request, 'Notas Adicionadas com Sucesso!')
        return redirect(f'/professor/{turmaid}')

def aula(request):
    if request.method=='POST':
        try:
        # Cadastrar aula
            turma = Turma.objects.get(id=request.POST['turma'])
            aula = Aula(turma=turma, data=request.POST['date'], desc=request.POST['description'])

            aula.save()
        # Cadastrar faltas
            faltas = []
            for i in request.POST:
                if i not in ['csrfmiddlewaretoken', 'turma', 'date', 'description']:
                    faltas.append(i)


            for f in faltas:
                aluno = Aluno.objects.get(id=f)
                falta = Falta.objects.get(aluno=aluno.id, turma=turma)
                falta.quantidade += 1
                falta.save()

        except ValueError:
            messages.error(request, 'Houve um erro ao cadastrar a aula.')
        
        
        return redirect(f'/professor/{request.POST["turma"]}')


def suporte(request):
    return render(request, 'pages/suporte.html')


def addalunos(request):
    if request.method == 'POST':
        doc = request.FILES['doc']
        turma_id = request.POST['turma']
        path = default_storage.save(f'uploads/alunos/{doc.name}', ContentFile(doc.read()))

        pd = pandas.read_excel(f'{os.getcwd()}/uploads/alunos/{doc.name}')

        for c in pd.iloc():
            username = c['User Account']

            if c['Registration Method'] != 'Teacher Manual enrollment':
                try:
                    aluno = Aluno.objects.get(username=username)
                except:
                    nome = c['First Name']
                    sobrenome = c['Last Name']
                    data_r = c['Registration Time']
                    ano, mes, dia = data_r[:10].split('-')

                    aluno = Aluno(username=username, nome=nome, sobrenome=sobrenome, data_inscricao=date(int(ano), int(mes), int(dia)))
                    aluno.save()

                try:
                    insc = Inscricao.objects.get(turma=turma_id, aluno=aluno.id)
                except:
                    turma = Turma.objects.get(id=turma_id)
                    insc = Inscricao(aluno=aluno, turma=turma)
                    insc.save()

                    faltas = Falta(turma_id = turma_id, aluno_id = aluno.id)
                    faltas.save()

        
        return redirect('/professor')
