from django.db import models
from gerenciamento.models import Paciente
from autenticacao.models import User
from datetime import datetime

TIPOS = (
    ("inicial", "Consulta Inicial"),
    ("evolucao", "Consulta de Evolução")
)


class Consulta(models.Model):
    data = models.DateTimeField(default=datetime.now)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=55, choices=TIPOS, default='inicial')

    def exibe_data(self):
        return self.data.date()


class Prontuario(models.Model):
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    finalizado = models.BooleanField(default=False)


class Observacoes(models.Model):
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    queixaPrincipal = models.CharField(max_length=255, blank=True, null=True)
    historiaAtual = models.CharField(max_length=255, blank=True, null=True)
    exameFisico = models.CharField(max_length=255, blank=True, null=True)
    avaliacaoFuncional = models.CharField(max_length=255, blank=True, null=True)
    historiaMedicamentosa = models.CharField(max_length=255, blank=True, null=True)
    examesComplementares = models.CharField(max_length=255, blank=True, null=True)


class Hipoteses(models.Model):
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    hipotese = models.CharField(max_length=255, blank=True, null=True)


class Prescricoes(models.Model):
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    exameSolicitado = models.CharField(max_length=255, blank=True, null=True)
    condutaTerapeutica = models.CharField(max_length=255, blank=True, null=True)
    medicamentos = models.CharField(max_length=255, blank=True, null=True)
    dieta = models.CharField(max_length=255, blank=True, null=True)
    orientacao = models.CharField(max_length=255, blank=True, null=True)
    encaminhamentos = models.CharField(max_length=255, blank=True, null=True)


class Sistema(models.Model):
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    cefaleia = models.BooleanField(default=False, blank=True, null=True)
    tonteiras = models.BooleanField(default=False, blank=True, null=True)
    convulsoes = models.BooleanField(default=False, blank=True, null=True)
    desmaio = models.BooleanField(default=False, blank=True, null=True)
    tremor = models.BooleanField(default=False, blank=True, null=True)
    difMemoria = models.BooleanField(default=False, blank=True, null=True)
    difAudicao = models.BooleanField(default=False, blank=True, null=True)
    zumbido = models.BooleanField(default=False, blank=True, null=True)
    difConcentracao = models.BooleanField(default=False, blank=True, null=True)
    difVisao = models.BooleanField(default=False, blank=True, null=True)
    difFalar = models.BooleanField(default=False, blank=True, null=True)
    difMastigar = models.BooleanField(default=False, blank=True, null=True)
    difPaladar = models.BooleanField(default=False, blank=True, null=True)
    difCheiro = models.BooleanField(default=False, blank=True, null=True)
    difEngolir = models.BooleanField(default=False, blank=True, null=True)
    resfriados = models.BooleanField(default=False, blank=True, null=True)
    roquidao = models.BooleanField(default=False, blank=True, null=True)
    alergia = models.BooleanField(default=False, blank=True, null=True)
    dispneia = models.BooleanField(default=False, blank=True, null=True)
    dorToracica = models.BooleanField(default=False, blank=True, null=True)
    tosse = models.BooleanField(default=False, blank=True, null=True)
    palpitacoes = models.BooleanField(default=False, blank=True, null=True)
    edema = models.BooleanField(default=False, blank=True, null=True)
    dormencia = models.BooleanField(default=False, blank=True, null=True)
    extremidadesFrias = models.BooleanField(default=False, blank=True, null=True)
    pirose = models.BooleanField(default=False, blank=True, null=True)
    probDigestivo = models.BooleanField(default=False, blank=True, null=True)
    nausea = models.BooleanField(default=False, blank=True, null=True)
    vomito = models.BooleanField(default=False, blank=True, null=True)
    dorAbdominal = models.BooleanField(default=False, blank=True, null=True)
    prisaoVentre = models.BooleanField(default=False, blank=True, null=True)
    diarreia = models.BooleanField(default=False, blank=True, null=True)
    hemorragiaDisgestiva = models.BooleanField(default=False, blank=True, null=True)
    constipacao = models.BooleanField(default=False, blank=True, null=True)
    incontFecal = models.BooleanField(default=False, blank=True, null=True)
    disfagia = models.BooleanField(default=False, blank=True, null=True)
    nicturia = models.BooleanField(default=False, blank=True, null=True)
    polidipsia = models.BooleanField(default=False, blank=True, null=True)
    disuria = models.BooleanField(default=False, blank=True, null=True)
    alguria = models.BooleanField(default=False, blank=True, null=True)
    urgMiccional = models.BooleanField(default=False, blank=True, null=True)
    hematuria = models.BooleanField(default=False, blank=True, null=True)
    incontUrinaria = models.BooleanField(default=False, blank=True, null=True)
    altJatoUrinario = models.BooleanField(default=False, blank=True, null=True)
    retUrinaria = models.BooleanField(default=False, blank=True, null=True)
    ativSexual = models.BooleanField(default=False, blank=True, null=True)
    corrimento = models.BooleanField(default=False, blank=True, null=True)
    pruidoVaginal = models.BooleanField(default=False, blank=True, null=True)
    sangramento = models.BooleanField(default=False, blank=True, null=True)
    fogacho = models.BooleanField(default=False, blank=True, null=True)
    probPele = models.BooleanField(default=False, blank=True, null=True)
    dorMuscular = models.BooleanField(default=False, blank=True, null=True)
    artralgia = models.BooleanField(default=False, blank=True, null=True)
    edemaArticular = models.BooleanField(default=False, blank=True, null=True)
    dorColuna = models.BooleanField(default=False, blank=True, null=True)
    difMovArticular = models.BooleanField(default=False, blank=True, null=True)
    difCaminhar = models.BooleanField(default=False, blank=True, null=True)
    queda = models.BooleanField(default=False, blank=True, null=True)
    ansiedade = models.BooleanField(default=False, blank=True, null=True)
    tristeza = models.BooleanField(default=False, blank=True, null=True)
    ideiaMorte = models.BooleanField(default=False, blank=True, null=True)
    altSono = models.BooleanField(default=False, blank=True, null=True)
    altPeso = models.BooleanField(default=False, blank=True, null=True)
    astenia = models.BooleanField(default=False, blank=True, null=True)
    febre = models.BooleanField(default=False, blank=True, null=True)
    sudorese = models.BooleanField(default=False, blank=True, null=True)
    usoAlcool = models.BooleanField(default=False, blank=True, null=True)
    usoFumo = models.BooleanField(default=False, blank=True, null=True)
    altApetite = models.BooleanField(default=False, blank=True, null=True)
