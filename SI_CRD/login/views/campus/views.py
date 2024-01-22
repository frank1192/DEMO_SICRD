from django.shortcuts import render
from django.views.generic import ListView
from login.models import *

# Create your views here.


class campuslistview(ListView):
    model=campus
    template_name='campus/list.html'
    def get_queryset(self):
        return campus.objects.all()
        #si quiero algun filtro en vez de .all ponemos .filter y hacemos el filtrado
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='listado de campus'
        #context['object_list']=escenario_deportivo.objects.all()
        return context
    




