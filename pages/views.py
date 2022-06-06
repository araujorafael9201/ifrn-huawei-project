from django.shortcuts import render

# EVENTOS
def ict_job_fair_brasil(request):
    return render(request, 'pages/ict-job-fair-brasil.html')

def ict_competition_brasil(request):
    return render(request, 'pages/ict-competition-brasil.html')

def seeds_for_the_future(request):
    return render(request, 'pages/seeds-for-the-future.html')



def index(request):
    return render(request, 'pages/index.html')

def instrutores(request):
    return render(request, 'pages/instrutores.html')

def certificacao(request):
    return render(request, 'pages/certificacao.html')

def contato(request):
    return render(request, 'pages/contato.html')

def laboratorios(request):
    return render(request, 'pages/laboratorios.html')
