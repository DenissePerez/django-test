# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 15:39
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acta',
            fields=[
                ('id_acta', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=300)),
                ('acta', models.FilePathField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Anexos',
            fields=[
                ('id_anexo', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('anexo', models.FilePathField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id_balance', models.CharField(max_length=8, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(b'^\\d{1,8}$')])),
                ('descripcion', models.CharField(max_length=200)),
                ('valor_compensado', models.DecimalField(decimal_places=2, max_digits=8)),
                ('valor_afectacion', models.DecimalField(decimal_places=2, max_digits=8)),
                ('valor_balance', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Coordinacion',
            fields=[
                ('id_coordinacion', models.CharField(max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(b'^\\d{1,10}$')])),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Coordinador',
            fields=[
                ('id_coordinador', models.CharField(max_length=12, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(b'^\\d{1,12}$')])),
                ('nombre', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=10)),
                ('id_coordinacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poda.Coordinacion')),
            ],
        ),
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id_expediente', models.CharField(max_length=5, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(b'^\\d{1,5}$')])),
                ('nombre', models.CharField(max_length=200)),
                ('resolucion', models.CharField(blank=True, max_length=12, null=True)),
                ('autorizacion', models.CharField(blank=True, max_length=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ficha_individuo',
            fields=[
                ('id_arbol', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('latitud', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
                ('longitud', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('familia', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=300)),
                ('altura', models.FloatField()),
                ('dap', models.FloatField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Informe_tecnico',
            fields=[
                ('id_informe', models.CharField(max_length=8, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(b'^\\d{1,8}$')])),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=300)),
                ('Informe', models.FilePathField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id_seguimiento', models.CharField(max_length=8, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(b'^\\d{1,8}$')])),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=300)),
                ('adjunto', models.FilePathField(null=True)),
                ('id_balance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poda.Balance')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitante',
            fields=[
                ('id_solicitante', models.CharField(max_length=30, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(b'^\\d{1,30}$')])),
                ('nombre', models.CharField(max_length=200)),
                ('cedula', models.IntegerField()),
                ('telefono', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=100)),
                ('barrio', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id_solicitud', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(default=b' ', max_length=100)),
                ('barrio', models.CharField(default=b' ', max_length=100)),
                ('municipio', models.CharField(default=b' ', max_length=100)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('id_anexo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poda.Anexos')),
                ('id_solicitante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poda.Solicitante')),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id_tecnico', models.CharField(max_length=12, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(b'^\\d{1,12}$')])),
                ('nombre', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=10)),
                ('id_coordinacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poda.Coordinacion')),
                ('id_solicitud', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poda.Solicitud')),
            ],
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id_visita', models.CharField(max_length=5, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(b'^\\d{1,10}$')])),
                ('detalles', models.CharField(max_length=300)),
                ('fecha', models.DateField()),
                ('id_acta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poda.Acta')),
                ('id_arbol', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poda.Ficha_individuo')),
                ('id_solicitud', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poda.Solicitud')),
            ],
        ),
        migrations.AddField(
            model_name='tecnico',
            name='id_visita',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poda.Visita'),
        ),
        migrations.AddField(
            model_name='seguimiento',
            name='id_visita',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poda.Visita'),
        ),
        migrations.AddField(
            model_name='expediente',
            name='id_solicitud',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poda.Solicitud'),
        ),
        migrations.AddField(
            model_name='coordinador',
            name='id_solicitud',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poda.Solicitud'),
        ),
    ]