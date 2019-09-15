from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('reserva/', reserva, name='reserva'),
    path("envio", recuperar, name='envio'),
    path('registro/', registro, name='registro'),
    path('envio2/', envio2, name='envio2'),
]