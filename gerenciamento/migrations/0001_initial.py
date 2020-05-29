# Generated by Django 2.2.12 on 2020-05-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=55)),
                ('dataNascimento', models.DateField()),
                ('estadoCivil', models.CharField(blank=True, max_length=55, null=True)),
                ('naturalidade', models.CharField(blank=True, max_length=55, null=True)),
                ('nacionalidade', models.CharField(blank=True, max_length=55, null=True)),
                ('cep', models.CharField(max_length=55)),
                ('endereco', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=11)),
                ('profissaoAtual', models.CharField(blank=True, max_length=55, null=True)),
                ('profissaoAnterior', models.CharField(blank=True, max_length=55, null=True)),
                ('renda', models.FloatField(blank=True, null=True)),
                ('codigo', models.CharField(max_length=7)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
    ]
