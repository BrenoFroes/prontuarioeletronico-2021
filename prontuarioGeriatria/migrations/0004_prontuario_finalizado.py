# Generated by Django 2.2.12 on 2020-06-18 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prontuarioGeriatria', '0003_auto_20200618_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='prontuario',
            name='finalizado',
            field=models.BooleanField(default=False),
        ),
    ]
