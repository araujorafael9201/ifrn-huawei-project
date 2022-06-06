from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # EVENTOS
    path('ict_job_fair_brasil/', views.ict_job_fair_brasil, name='ict_job_fair_brasil'),
    path('ict_competition_brasil/', views.ict_competition_brasil, name='ict_competition_brasil'),
    path('seeds_for_the_future/', views.seeds_for_the_future, name='seeds_for_the_future'),

    path('laboratorios/', views.laboratorios, name='laboratorios'),
    path('instrutores/', views.instrutores, name='instrutores'),
    path('certificacao/', views.certificacao, name='cerficacao'),
    path('contato/', views.contato, name='contato'),
]
