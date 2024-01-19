from django.db import models
from datetime import *
# Create your models here.
# Creacion de modelos basicops para el demo del aplicativo, consta que no
# cuenta aun con las equivalencia sobre la informacion de los usuarios
# no hay conexion con sira .


class campus (models.Model):
    name=models.CharField(max_length=150,verbose_name='Nombre')
    id=models.CharField(max_length=15,unique=True,verbose_name='Identificacion',primary_key=True)
    def __str__(self):
        return f'{self.name} - {self.id}'
    
    class Meta:
        verbose_name='campus'
        verbose_name_plural='campus'
        db_table='campus'
        ordering=['id']
    
class facultades (models.Model):
    name=models.CharField(max_length=150,verbose_name='Nombre')
    id=models.CharField(max_length=15,unique=True,verbose_name='Identificacion',primary_key=True)
    campus=models.ForeignKey(campus, on_delete=models.PROTECT)
    def __str__(self):
        return f'{self.name} - {self.id} - {self.campus}'
    
    class Meta:
        verbose_name='facultad'
        verbose_name_plural='facultades'
        db_table='facultades'
        ordering=['id']

class programas_academicos (models.Model):
    name=models.CharField(max_length=150,verbose_name='Nombre')
    id=models.CharField(max_length=4,unique=True,verbose_name='Codigo Programa',primary_key=True)
    facultad=models.ForeignKey(facultades, on_delete=models.PROTECT)
    def __str__(self):
        return f'{self.name} - {self.id} - {self.facultad}'
    
    class Meta:
        verbose_name='programa academico'
        verbose_name_plural='programas academicos'
        db_table='programas academicos'
        ordering=['id']
        
class estamento (models.Model):
    id=models.CharField(max_length=2,unique=True,verbose_name='Codigo',primary_key=True)
    name=models.CharField(max_length=150,verbose_name='Nombre')
    def __str__(self):
        return f'{self.name} - {self.id}'
    
    class Meta:
        verbose_name='estamento'
        verbose_name_plural='estamentos'
        db_table='estamento'
        ordering=['id']
    
class usuario (models.Model):
    id=models.CharField(max_length=11,unique=True,verbose_name='Identificacion',primary_key=True)
    codigo=models.CharField(max_length=10,unique=True,verbose_name='codigo')
    name=models.CharField(max_length=150,verbose_name='Nombre')
    apellidos=models.CharField(max_length=150,verbose_name='Apellidos')
    age= models.PositiveIntegerField(default=0,verbose_name='edad')
    genero=models.CharField(max_length=150,verbose_name='genero')
    programas_academico=models.ForeignKey(programas_academicos,on_delete=models.PROTECT,verbose_name='Programa academico')
    facultad=models.ForeignKey(facultades,on_delete=models.PROTECT,verbose_name='facultad')
    estamento=models.ForeignKey(estamento,on_delete=models.PROTECT,verbose_name='estamento')
    estado= models.CharField(max_length=150,verbose_name='estado')
    
    def __str__(self):
        return f'{self.name} {self.apellidos} - {self.id} - {self.codigo} - {self.programas_academico} - {self.facultad} - {self.estamento}'
    
    class Meta:
        verbose_name='usuario'
        verbose_name_plural='usuarios'
        db_table='usuario'
        ordering=['id']
    
class escenario_deportivo (models.Model):
    name=models.CharField(max_length=150,verbose_name='Nombre')
    id=models.CharField(max_length=15,unique=True,verbose_name='Identificacion',primary_key=True)
    estado=models.CharField(max_length=20,verbose_name='Estado')
    campus=models.ForeignKey(campus, on_delete=models.PROTECT)
    
    def __str__(self):
        return f'{self.name} - {self.id} - {self.estado} - {self.campus}'
    
    class Meta:
        verbose_name='escenario deportivo'
        verbose_name_plural='escenario deportivos'
        db_table='escenario deportivos'
        ordering=['id']
        
class Asistencia(models.Model):
    escenario = models.ForeignKey(escenario_deportivo, on_delete=models.CASCADE, verbose_name='Escenario deportivo')
    usuario = models.ForeignKey(usuario, on_delete=models.PROTECT, verbose_name='Usuario')
    fecha = models.DateField(verbose_name='Fecha')
    hora = models.TimeField(verbose_name='Hora')

    def __str__(self):
        return f'{self.usuario} - {self.escenario} - {self.fecha} - {self.hora}'

    class Meta:
        verbose_name = 'asistencia'
        verbose_name_plural = 'asistencias'
        db_table = 'asistencias'
        ordering = ['fecha', 'hora']
        
class prueba(models.Model):
    fecha = models.DateField(verbose_name='Fecha')
    hora = models.TimeField(verbose_name='Hora')

    def __str__(self):
        return f'{self.fecha} - {self.hora}'

    class Meta:
        verbose_name = 'prueba'
        verbose_name_plural = 'prueba'
        db_table = 'prueba'
        ordering = ['fecha', 'hora']

