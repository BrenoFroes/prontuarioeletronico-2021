from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=55)
    dataNascimento = models.DateField()
    estadoCivil = models.CharField(max_length=55, blank=True, null=True)
    naturalidade = models.CharField(max_length=55, blank=True, null=True)
    nacionalidade = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        abstract = True


class Paciente(Pessoa):
    cep = models.CharField(max_length=55)
    endereco = models.CharField(max_length=100)
    tel = models.CharField(max_length=11)
    profissaoAtual = models.CharField(max_length=55, blank=True, null=True)
    profissaoAnterior = models.CharField(max_length=55, blank=True, null=True)
    renda = models.FloatField(blank=True, null=True)


class Medico(Pessoa):
    crm = models.CharField(max_length=55)
