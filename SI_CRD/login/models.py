from django.db import models
from datetime import datetime
# Create your models here.

class campus (models.Model):
    name=models.CharField(max_length=150,verbose_name='Nombre')
    id=models.CharField(max_length=15,unique=True,verbose_name='Identificacion',primary_key=True)

    

class facultades (models.Model):
    name=models.CharField(max_length=150,verbose_name='Nombre')
    id=models.CharField(max_length=15,unique=True,verbose_name='Identificacion',primary_key=True)
    campus=models.ForeignKey(campus, on_delete=models.PROTECT)

class programas_academicos (models.Model):
    name=models.CharField(max_length=150,verbose_name='Nombre')
    id=models.CharField(max_length=4,unique=True,verbose_name='Codigo Programa',primary_key=True)
    facultad=models.ForeignKey(facultades, on_delete=models.PROTECT)

class escenario_deportivo (models.Model):
    name=models.CharField(max_length=150,verbose_name='Nombre')
    id=models.CharField(max_length=15,unique=True,verbose_name='Identificacion',primary_key=True)
    estado=models.CharField(max_length=20,verbose_name='Estado')
    campus=models.ForeignKey(campus, on_delete=models.PROTECT)
    asistencia= models


