from django.urls import path
from login.views import *
from login.views.campus.views import *
from login.views.escenarios_deportivos.views import *

app_name='muestras'
urlpatterns = [
    path('campus/list/',campuslistview.as_view(), name='listado de campus'),
    path('escenarios_deportivos/list/',escenarios_deportivoslistview.as_view(), name='listado de escenarios deportivos'),

]
#escenarios_deportivoslistview