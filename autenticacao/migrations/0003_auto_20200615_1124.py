# Generated by Django 2.2.12 on 2020-06-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0002_auto_20200608_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='e-mail'),
        ),
    ]
