from django.db import models
from gerenciamento.models import Paciente, Medico


class Consulta(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)


class Prontuario(models.Model):
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    codigo = models.IntegerField()


class Observacoes(models.Model):
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    queixaPrincipal = models.CharField(max_length=100, blank=True, null=True)
    historiaAtual = models.CharField(max_length=100, blank=True, null=True)
    historiaPregressa = models.CharField(max_length=100, blank=True, null=True)
    historiaFisiologica = models.CharField(max_length=100, blank=True, null=True)
    historiaSocial = models.CharField(max_length=100, blank=True, null=True)
    historiaFamiliar = models.CharField(max_length=100, blank=True, null=True)
    exameFisico = models.CharField(max_length=100, blank=True, null=True)
    avaliacaoFuncional = models.CharField(max_length=100, blank=True, null=True)
    historiaMedicamentosa = models.CharField(max_length=100, blank=True, null=True)
    examesComplementares = models.CharField(max_length=100, blank=True, null=True)


class Hipoteses(models.Model):
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    hipotese = models.CharField(max_length=100, blank=True, null=True)


class Prescricoes(models.Model):
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    hipotese = models.CharField(max_length=100, blank=True, null=True)
