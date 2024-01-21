from django.urls import path
from login.views import *
from login.views.campus.views import campus_list
app_name='muestras'
urlpatterns = [
    path('campus/list/',campus_list, name='listado de campus'),
]