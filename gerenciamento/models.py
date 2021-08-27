from django.db import models
from datetime import datetime
from autenticacao.models import User


class Pessoa(models.Model):
    nome = models.CharField(max_length=55)
    dataNascimento = models.DateField()
    estadoCivil = models.CharField(max_length=55, blank=True, null=True)
    naturalidade = models.CharField(max_length=55, blank=True, null=True)
    nacionalidade = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ('nome',)
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return self.nome

    def idade(self):
        if self.dataNascimento:
            hoje = datetime.today().date()
            idade = hoje.year - self.dataNascimento.year
            if hoje.month < self.dataNascimento.month or (
                    hoje.month == self.dataNascimento.month and hoje.day < self.dataNascimento.day):
                idade -= 1
            return idade


class Paciente(Pessoa):
    id = models.AutoField(primary_key=True)
    cep = models.CharField(max_length=55)
    endereco = models.CharField(max_length=100)
    tel = models.CharField(max_length=11)
    cpf = models.CharField(unique=True, max_length=11)
    cns = models.CharField(blank=True, null=True, max_length=15)
    escolaridade = models.CharField(max_length=255)
    genero = models.IntegerField(default=1)
    profissaoAtual = models.CharField(max_length=55, blank=True, null=True)
    profissaoAnterior = models.CharField(max_length=55, blank=True, null=True)
    renda = models.FloatField(blank=True, null=True)
    codigo = models.CharField(max_length=8)  # número do prontuário que identifica o usuário

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = "Pacientes"

    def clean_something_unique_or_null(self):
        if self.cleaned_data['something_unique_or_null'] == "":
            return None
        else:
            return self.cleaned_data['something_unique_or_null']


class Historico(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    historiaPregressa = models.CharField(max_length=255, blank=True, null=True)
    historiaFisiologica = models.CharField(max_length=255, blank=True, null=True)
    historiaSocial = models.CharField(max_length=255, blank=True, null=True)
    historiaFamiliar = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Histórico'
        verbose_name_plural = "Históricos"
