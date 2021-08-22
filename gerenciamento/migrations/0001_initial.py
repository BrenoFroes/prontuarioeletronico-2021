# Generated by Django 3.2 on 2021-08-22 19:05

from django.db import migrations, models
import django.db.models.deletion
from django.contrib.postgres.operations import HStoreExtension

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('nome', models.CharField(max_length=55)),
                ('dataNascimento', models.DateField()),
                ('estadoCivil', models.CharField(blank=True, max_length=55, null=True)),
                ('naturalidade', models.CharField(blank=True, max_length=55, null=True)),
                ('nacionalidade', models.CharField(blank=True, max_length=55, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cep', models.CharField(max_length=55)),
                ('endereco', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=11)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('cns', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('escolaridade', models.CharField(max_length=255)),
                ('genero', models.IntegerField(default=1)),
                ('profissaoAtual', models.CharField(blank=True, max_length=55, null=True)),
                ('profissaoAnterior', models.CharField(blank=True, max_length=55, null=True)),
                ('renda', models.FloatField(blank=True, null=True)),
                ('codigo', models.CharField(max_length=8)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('historiaPregressa', models.CharField(blank=True, max_length=255, null=True)),
                ('historiaFisiologica', models.CharField(blank=True, max_length=255, null=True)),
                ('historiaSocial', models.CharField(blank=True, max_length=255, null=True)),
                ('historiaFamiliar', models.CharField(blank=True, max_length=255, null=True)),
                ('paciente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gerenciamento.paciente')),
            ],
            options={
                'verbose_name': 'Histórico',
                'verbose_name_plural': 'Históricos',
            },
        ),
    ]
