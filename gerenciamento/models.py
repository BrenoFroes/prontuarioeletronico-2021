from django.db import models
from datetime import datetime, timezone


class Pessoa(models.Model):
    nome = models.CharField(max_length=55)
    dataNascimento = models.DateField()
    estadoCivil = models.CharField(max_length=55, blank=True, null=True)
    naturalidade = models.CharField(max_length=55, blank=True, null=True)
    nacionalidade = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ('nome', )

    def __str__(self):
        return self.nome

    def idade(self):
        if self.dataNascimento:
            hoje = datetime.today().date()
            idade = hoje.year - self.dataNascimento.year
            if hoje.month < self.dataNascimento.month or (hoje.month == self.dataNascimento.month and hoje.day < self.dataNascimento.day):
                idade -= 1
            return idade

class Paciente(Pessoa):
    cep = models.CharField(max_length=55)
    endereco = models.CharField(max_length=100)
    tel = models.CharField(max_length=11)
    profissaoAtual = models.CharField(max_length=55, blank=True, null=True)
    profissaoAnterior = models.CharField(max_length=55, blank=True, null=True)
    renda = models.FloatField(blank=True, null=True)


class Medico(Pessoa):
    crm = models.CharField(max_length=55)
