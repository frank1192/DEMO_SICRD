from django.shortcuts import render
from login.models import *
# Create your views here.

def campus_list(request):
    data = {
        'title' : ' listado de campus',
        'name' : 'Franklin',
        'campus' : campus.objects.all()
    }
    return render(request,'campus/list.html',data)

def misegundavista(request):
    data = {
        'name' : 'Franklin',
        'programas_academicos' : programas_academicos.objects.all(),
        'escenario_deportivos' : escenario_deportivo.objects.all()
    }
    return render(request,'second.html',data)