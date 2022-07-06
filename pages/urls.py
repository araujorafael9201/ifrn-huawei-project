from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre_ict_academy', views.sobre_ict_academy, name='sobre_ict_academy'),
    path('sobre_huawei', views.sobre_huawei, name='sobre_huawei'),
    path('cloud_service', views.cloud_service, name='cloud_service'),
    path('inteligencia_artificial', views.inteligencia_artificial, name='inteligencia_artificial'),
    path('datacom', views.datacom, name='datacom'),
    path('5g', views.cincog, name='5g'),
    path('ict_job_fair_brasil/', views.ict_job_fair_brasil, name='ict_job_fair_brasil'),
    path('ict_competition_brasil/', views.ict_competition_brasil, name='ict_competition_brasil'),
    path('seeds_for_the_future/', views.seeds_for_the_future, name='seeds_for_the_future'),
    path('laboratorios/', views.laboratorios, name='laboratorios'),
    path('instrutores/', views.instrutores, name='instrutores'),
    path('certificacao/', views.certificacao, name='cerficacao'),
    path('hands-on/', views.hands_on, name='hands-on'),
    path('contato/', views.contato, name='contato'),
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
    path('matricula/', views.matricula, name='matricula'),
    # path('addnotas/', views.add_notas, name="addnotas")
    # n funciona isso aq
    # path('docs/uploads/<docname>', views.docs, name='docs')
]
