# Generated by Django 5.0.1 on 2024-01-19 05:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='campus',
            fields=[
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='Identificacion')),
            ],
            options={
                'verbose_name': 'campus',
                'verbose_name_plural': 'campus',
                'db_table': 'campus',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='estamento',
            fields=[
                ('id', models.CharField(max_length=2, primary_key=True, serialize=False, unique=True, verbose_name='Codigo')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'estamento',
                'verbose_name_plural': 'estamentos',
                'db_table': 'estamento',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='escenario_deportivo',
            fields=[
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='Identificacion')),
                ('estado', models.CharField(max_length=20, verbose_name='Estado')),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='login.campus')),
            ],
            options={
                'verbose_name': 'escenario deportivo',
                'verbose_name_plural': 'escenario deportivos',
                'db_table': 'escenario deportivos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='facultades',
            fields=[
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='Identificacion')),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='login.campus')),
            ],
            options={
                'verbose_name': 'facultad',
                'verbose_name_plural': 'facultades',
                'db_table': 'facultades',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='programas_academicos',
            fields=[
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False, unique=True, verbose_name='Codigo Programa')),
                ('facultad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='login.facultades')),
            ],
            options={
                'verbose_name': 'programa academico',
                'verbose_name_plural': 'programas academicos',
                'db_table': 'programas academicos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True, verbose_name='Identificacion')),
                ('codigo', models.CharField(max_length=10, unique=True, verbose_name='codigo')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('age', models.PositiveIntegerField(default=0, verbose_name='edad')),
                ('genero', models.CharField(max_length=150, verbose_name='genero')),
                ('estado', models.CharField(max_length=150, verbose_name='estado')),
                ('estamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='login.estamento', verbose_name='estamento')),
                ('facultad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='login.facultades', verbose_name='facultad')),
                ('programas_academico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='login.programas_academicos', verbose_name='Programa academico')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
                'db_table': 'usuario',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('hora', models.TimeField(verbose_name='Hora')),
                ('escenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.escenario_deportivo', verbose_name='Escenario deportivo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='login.usuario', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'asistencia',
                'verbose_name_plural': 'asistencias',
                'db_table': 'asistencias',
                'ordering': ['fecha', 'hora'],
            },
        ),
    ]
