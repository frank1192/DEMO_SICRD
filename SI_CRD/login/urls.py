from django.urls import path
from login.views import *
app_name='muestras'
urlpatterns = [
    path('uno/',miprimeravista, name='Programas-academicos'),
    path('dos/',misegundavista,name='escenarios-deportivos')
]