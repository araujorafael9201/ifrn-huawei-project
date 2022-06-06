from django.shortcuts import render

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
