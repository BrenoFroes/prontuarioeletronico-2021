# Generated by Django 2.2.12 on 2021-07-26 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prontuarioGeriatria', '0015_auto_20210723_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sistema',
            name='sintoma',
        ),
    ]
