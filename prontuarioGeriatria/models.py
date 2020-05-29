from django.db import models
from gerenciamento.models import Paciente
from autenticacao.models import User

TIPOS = (
    ("inicial", "Consulta Inicial"),
    ("evolucao", "Consulta de Evolução")
)


class Consulta(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=55, choices=TIPOS, default='inicial')


class Prontuario(models.Model):
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)


class Observacoes(models.Model):
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    queixaPrincipal = models.CharField(max_length=255, blank=True, null=True)
    historiaAtual = models.CharField(max_length=255, blank=True, null=True)
    historiaPregressa = models.CharField(max_length=255, blank=True, null=True)
    historiaFisiologica = models.CharField(max_length=255, blank=True, null=True)
    historiaSocial = models.CharField(max_length=255, blank=True, null=True)
    historiaFamiliar = models.CharField(max_length=255, blank=True, null=True)
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
    cefaleia = models.BooleanField(default=False)
    tonteiras = models.BooleanField(default=False)
    convulsoes = models.BooleanField(default=False)
    desmaio = models.BooleanField(default=False)
    tremor = models.BooleanField(default=False)
    difMemoria = models.BooleanField(default=False)
    difAudicao = models.BooleanField(default=False)
    zumbido = models.BooleanField(default=False)
    difConcentracao = models.BooleanField(default=False)
    difVisao = models.BooleanField(default=False)
    difFalar = models.BooleanField(default=False)
    difMastigar = models.BooleanField(default=False)
    difPaladar = models.BooleanField(default=False)
    difCheiro = models.BooleanField(default=False)
    difEngolir = models.BooleanField(default=False)
    resfriados = models.BooleanField(default=False)
    roquidao = models.BooleanField(default=False)
    alergia = models.BooleanField(default=False)
    dispneia = models.BooleanField(default=False)
    dorToracica = models.BooleanField(default=False)
    tosse = models.BooleanField(default=False)
    palpitacoes = models.BooleanField(default=False)
    edema = models.BooleanField(default=False)
    dormencia = models.BooleanField(default=False)
    extremidadesFrias = models.BooleanField(default=False)
    pirose = models.BooleanField(default=False)
    probDigestivo = models.BooleanField(default=False)
    nausea = models.BooleanField(default=False)
    vomito = models.BooleanField(default=False)
    dorAbdominal = models.BooleanField(default=False)
    prisaoVentre = models.BooleanField(default=False)
    diarreia = models.BooleanField(default=False)
    hemorragiaDisgestiva = models.BooleanField(default=False)
    constipacao = models.BooleanField(default=False)
    incontFecal = models.BooleanField(default=False)
    disfagia = models.BooleanField(default=False)
    nicturia = models.BooleanField(default=False)
    polidipsia = models.BooleanField(default=False)
    disuria = models.BooleanField(default=False)
    alguria = models.BooleanField(default=False)
    urgMiccional = models.BooleanField(default=False)
    hematuria = models.BooleanField(default=False)
    incontUrinaria = models.BooleanField(default=False)
    altJatoUrinario = models.BooleanField(default=False)
    retUrinaria = models.BooleanField(default=False)
    ativSexual = models.BooleanField(default=False)
    corrimento = models.BooleanField(default=False)
    pruidoVaginal = models.BooleanField(default=False)
    sangramento = models.BooleanField(default=False)
    fogacho = models.BooleanField(default=False)
    probPele = models.BooleanField(default=False)
    dorMuscular = models.BooleanField(default=False)
    artralgia = models.BooleanField(default=False)
    edemaArticular = models.BooleanField(default=False)
    dorColuna = models.BooleanField(default=False)
    difMovArticular = models.BooleanField(default=False)
    difCaminhar = models.BooleanField(default=False)
    queda = models.BooleanField(default=False)
    ansiedade = models.BooleanField(default=False)
    tristeza = models.BooleanField(default=False)
    ideiaMorte = models.BooleanField(default=False)
    altSono = models.BooleanField(default=False)
    altPeso = models.BooleanField(default=False)
    astenia = models.BooleanField(default=False)
    febre = models.BooleanField(default=False)
    sudorese = models.BooleanField(default=False)
    usoAlcool = models.BooleanField(default=False)
    usoFumo = models.BooleanField(default=False)
    altApetite = models.BooleanField(default=False)
