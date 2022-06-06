from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='indexs'),
    path('sobre_ict_academy', views.sobre_ict_academy, name='sobre_ict_academy'),
    path('sobre_huawei', views.sobre_huawei, name='sobre_huawei'),
    path('cloud_service', views.cloud_service, name='cloud_service'),
    path('inteligencia_artificial', views.inteligencia_artificial, name='inteligencia_artificial'),
    path('datacom', views.datacom, name='datacom'),
    path('5g', views.cincog, name='5g')
]
