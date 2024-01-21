from django.shortcuts import render
from login.models import *
# Create your views here.

def miprimeravista(request):
    data = {
        'name' : 'Franklin',
        'programas_academicos' : programas_academicos.objects.all()
    }
    return render(request,'home.html',data)

def misegundavista(request):
    data = {
        'name' : 'Franklin',
        'programas_academicos' : programas_academicos.objects.all(),
        'escenario_deportivos' : escenario_deportivo.objects.all()
    }
    return render(request,'second.html',data)