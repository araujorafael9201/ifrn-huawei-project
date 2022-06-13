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
    path('contato/', views.contato, name='contato'),
    path('inscricao/', views.inscricao, name='inscricao'),
    path('inscrever/', views.inscrever, name='inscrever'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.login, name='login'),
    path('logar/', views.logar, name='logar'),
    path('deslogar/', views.deslogar, name='deslogar')
]
