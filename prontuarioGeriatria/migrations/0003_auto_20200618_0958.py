# Generated by Django 2.2.12 on 2020-06-18 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prontuarioGeriatria', '0002_auto_20200615_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observacoes',
            name='historiaFamiliar',
        ),
        migrations.RemoveField(
            model_name='observacoes',
            name='historiaFisiologica',
        ),
        migrations.RemoveField(
            model_name='observacoes',
            name='historiaPregressa',
        ),
        migrations.RemoveField(
            model_name='observacoes',
            name='historiaSocial',
        ),
    ]