# Generated by Django 3.2 on 2021-08-22 19:05

import datetime
from django.conf import settings
import django.contrib.postgres.fields.hstore
from django.contrib.postgres.operations import HStoreExtension
from django.db import migrations, models
import django.db.models.deletion
import prontuarioGeriatria.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gerenciamento', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateTimeField(default=datetime.datetime.now)),
                ('tipo', models.CharField(choices=[('inicial', 'Consulta Inicial'), ('evolucao', 'Consulta de Evolução')], default='inicial', max_length=55)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerenciamento.paciente')),
            ],
            options={
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consultas',
                'ordering': ['data'],
            },
        ),
        migrations.CreateModel(
            name='Prontuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('finalizado', models.BooleanField(default=False)),
                ('consulta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='prontuarioGeriatria.consulta')),
            ],
            options={
                'verbose_name': 'Prontuário',
                'verbose_name_plural': 'Prontuários',
                'ordering': ['data'],
            },
        ),
        migrations.CreateModel(
            name='TestesNeuropsicologicos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cdr', models.IntegerField(blank=True, null=True)),
                ('mmse', models.IntegerField(blank=True, null=True)),
                ('cdt', models.IntegerField(blank=True, null=True)),
                ('depressao', models.BooleanField(blank=True, null=True)),
                ('lawton', models.IntegerField(blank=True, null=True)),
                ('tmt', models.IntegerField(blank=True, null=True)),
                ('cerad', models.IntegerField(blank=True, null=True)),
                ('prontuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='prontuarioGeriatria.prontuario')),
            ],
            options={
                'verbose_name': 'Teste Neuropsicológico',
                'verbose_name_plural': 'Testes Neuropsicológicos',
                'ordering': ['prontuario'],
            },
        ),
        migrations.CreateModel(
            name='TesteComputadorizadoAtencaoVisual',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tcaIncorretas', models.IntegerField(blank=True, null=True)),
                ('tcaOmitidas', models.IntegerField(blank=True, null=True)),
                ('tcaTempoReacao', models.IntegerField(blank=True, null=True)),
                ('tcaVariabilidadeTempoReacao', models.BooleanField(blank=True, null=True)),
                ('testeNeuro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='prontuarioGeriatria.testesneuropsicologicos')),
            ],
            options={
                'verbose_name': 'TCA',
                'verbose_name_plural': "TCA's",
                'ordering': ['testeNeuro'],
            },
        ),
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sintomas', django.contrib.postgres.fields.hstore.HStoreField(default=prontuarioGeriatria.models.jsonfield_default_value)),
                ('prontuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='prontuarioGeriatria.prontuario')),
            ],
            options={
                'verbose_name': 'Sistema',
                'verbose_name_plural': 'Sistemas',
                'ordering': ['prontuario'],
            },
        ),
        migrations.CreateModel(
            name='Prescricoes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('exameSolicitado', models.CharField(blank=True, max_length=255, null=True)),
                ('condutaTerapeutica', models.CharField(blank=True, max_length=255, null=True)),
                ('medicamentos', models.CharField(blank=True, max_length=255, null=True)),
                ('dieta', models.CharField(blank=True, max_length=255, null=True)),
                ('orientacao', models.CharField(blank=True, max_length=255, null=True)),
                ('encaminhamentos', models.CharField(blank=True, max_length=255, null=True)),
                ('prontuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='prontuarioGeriatria.prontuario')),
            ],
            options={
                'verbose_name': 'Prescrição',
                'verbose_name_plural': 'Prescrições',
                'ordering': ['prontuario'],
            },
        ),
        migrations.CreateModel(
            name='Observacoes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('testeNeuropsicologico', models.IntegerField(blank=True, null=True)),
                ('queixaPrincipal', models.CharField(blank=True, max_length=255, null=True)),
                ('historiaAtual', models.CharField(blank=True, max_length=255, null=True)),
                ('exameFisico', models.CharField(blank=True, max_length=255, null=True)),
                ('avaliacaoFuncional', models.CharField(blank=True, max_length=255, null=True)),
                ('historiaMedicamentosa', models.CharField(blank=True, max_length=255, null=True)),
                ('examesComplementares', models.CharField(blank=True, max_length=255, null=True)),
                ('prontuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='prontuarioGeriatria.prontuario')),
            ],
            options={
                'verbose_name': 'Observação',
                'verbose_name_plural': 'Observações',
                'ordering': ['prontuario'],
            },
        ),
        migrations.CreateModel(
            name='Hipoteses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hipotese', models.CharField(blank=True, max_length=255, null=True)),
                ('prontuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='prontuarioGeriatria.prontuario')),
            ],
            options={
                'verbose_name': 'Hipótese',
                'verbose_name_plural': 'Hipóteses',
                'ordering': ['prontuario'],
            },
        ),
    ]
