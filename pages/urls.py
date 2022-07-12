from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('laboratorios/', views.laboratorios, name='laboratorios'),
    path('instrutores/', views.instrutores, name='instrutores'),
    path('certificacao/', views.certificacao, name='cerficacao'),
    path('contato/', views.contato, name='contato'),

    ## SOBRE
    path('ict_academy', views.sobre_ict_academy, name='ict-academy'),
    path('huawei', views.sobre_huawei, name='huawei'),

    ## CURSOS
    path('5g-networks', views.cincog, name='5g-networks'),
    path('artificial-intelligence', views.inteligencia_artificial, name='artificial-intelligence'),
    path('cloud-service', views.cloud_service, name='cloud-service'),
    path('datacom', views.datacom, name='datacom'),
    path('hands-on/', views.hands_on, name='hands-on'),

    # EVENTOS
    path('ict-competition-brasil/', views.ict_competition_brasil, name='ict-competition-brasil'),
    path('ict-job-fair-brasil/', views.ict_job_fair_brasil, name='ict-job-fair-brasil'),
    path('seeds-for-the-future/', views.seeds_for_the_future, name='seeds-for-the-future'),


    # NAO CLASSIFICADOS
    path('inscricao/', views.inscricao, name='inscricao'),
    path('inscrever/', views.inscrever, name='inscrever'),
    path('desinscrever/', views.desinscrever, name='desinscrever'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.login, name='login'),
    path('logar/', views.logar, name='logar'),
    path('deslogar/', views.deslogar, name='deslogar'),
    path('professor/', views.professor, name='professor'),
    path('proflogin/', views.professor_login, name='proflogin'),
    path('proflogar/', views.professor_logar, name='proflogar'),
    path('aluno/', views.aluno, name='alunoinfo'),
    path('turmainfo/<int:id>', views.turmainfo, name='turmainfo'),
    path('notas/', views.notas, name='notas'),
]
