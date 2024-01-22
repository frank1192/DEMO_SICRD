from django.views.generic import ListView
from login.models import *

# Create your views here.


class escenarios_deportivoslistview(ListView):
    model=escenario_deportivo
    template_name='escenarios_deportivos/list.html'
    def get_queryset(self):
        return escenario_deportivo.objects.all()
        #si quiero algun filtro en vez de .all ponemos .filter y hacemos el filtrado
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='listado de escenarios deportivos univalle'
        #context['object_list']=escenario_deportivo.objects.all()
        return context
    



