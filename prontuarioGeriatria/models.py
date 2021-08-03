from django.contrib.postgres.fields import HStoreField

from gerenciamento.models import Paciente
from autenticacao.models import User
from datetime import datetime
from django.db import models

TIPOS = (
    ("inicial", "Consulta Inicial"),
    ("evolucao", "Consulta de Evolução")
)


class Consulta(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateTimeField(default=datetime.now)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=55, choices=TIPOS, default='inicial')

    def exibe_data(self):
        return self.data.date()

    class Meta:
        ordering = ["data"]
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"


class Prontuario(models.Model):
    id = models.AutoField(primary_key=True)
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    finalizado = models.BooleanField(default=False)

    class Meta:
        ordering = ["data"]
        verbose_name = "Prontuário"
        verbose_name_plural = "Prontuários"

class Observacoes(models.Model):
    id = models.AutoField(primary_key=True)
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    queixaPrincipal = models.CharField(max_length=255, blank=True, null=True)
    historiaAtual = models.CharField(max_length=255, blank=True, null=True)
    exameFisico = models.CharField(max_length=255, blank=True, null=True)
    avaliacaoFuncional = models.CharField(max_length=255, blank=True, null=True)
    historiaMedicamentosa = models.CharField(max_length=255, blank=True, null=True)
    examesComplementares = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ["prontuario"]
        verbose_name = "Observação"
        verbose_name_plural = "Observações"

class Hipoteses(models.Model):
    id = models.AutoField(primary_key=True)
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    hipotese = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ["prontuario"]
        verbose_name = "Hipótese"
        verbose_name_plural = "Hipóteses"


class Prescricoes(models.Model):
    id = models.AutoField(primary_key=True)
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    exameSolicitado = models.CharField(max_length=255, blank=True, null=True)
    condutaTerapeutica = models.CharField(max_length=255, blank=True, null=True)
    medicamentos = models.CharField(max_length=255, blank=True, null=True)
    dieta = models.CharField(max_length=255, blank=True, null=True)
    orientacao = models.CharField(max_length=255, blank=True, null=True)
    encaminhamentos = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ["prontuario"]
        verbose_name = "Prescrição"
        verbose_name_plural = "Prescrições"

def jsonfield_default_value():
    jsonDefault = '{"cefaleia": "",' \
                  '"tonteiras": "",' \
                  '"convulsoes": "",' \
                  '"desmaio": "",' \
                  '"tremor": "",' \
                  '"difMemoria": "",' \
                  '"difAudicao": "",' \
                  '"zumbido": "",' \
                  '"difConcentracao": "",' \
                  '"difVisao": "",' \
                  '"difFalar": "",' \
                  '"difMastigar": "",' \
                  '"difPaladar": "",' \
                  '"difCheiro": "",' \
                  '"difEngolir": "",' \
                  '"resfriados": "",' \
                  '"roquidao": "",' \
                  '"alergia": "",' \
                  '"dispneia": "",' \
                  '"dorToracica": "",' \
                  '"tosse": "",' \
                  '"palpitacoes": "",' \
                  '"edema": "",' \
                  '"dormencia": "",' \
                  '"extremidadesFrias": "",' \
                  '"pirose": "",' \
                  '"probDigestivo": "",' \
                  '"nausea": "",' \
                  '"vomito": "",' \
                  '"dorAbdominal": "",' \
                  '"prisaoVentre": "",' \
                  '"diarreia": "",' \
                  '"hemorragiaDisgestiva": "",' \
                  '"constipacao": "",' \
                  '"incontFecal": "",' \
                  '"disfagia": "",' \
                  '"nicturia": "",' \
                  '"polidipsia": "",' \
                  '"disuria": "",' \
                  '"alguria": "",' \
                  '"urgMiccional": "",' \
                  '"hematuria": "",' \
                  '"incontUrinaria": "",' \
                  '"altJatoUrinario": "",' \
                  '"retUrinaria": "",' \
                  '"ativSexual": "",' \
                  '"corrimento": "",' \
                  '"pruidoVaginal": "",' \
                  '"sangramento": "",' \
                  '"fogacho": "",' \
                  '"probPele": "",' \
                  '"dorMuscular": "",' \
                  '"artralgia": "",' \
                  '"edemaArticular": "",' \
                  '"dorColuna": "",' \
                  '"difMovArticular": "",' \
                  '"difCaminhar": "",' \
                  '"queda": "",' \
                  '"ansiedade": "",' \
                  '"tristeza": "",' \
                  '"ideiaMorte": "",' \
                  '"altSono": "",' \
                  '"altPeso": "",' \
                  '"astenia": "",' \
                  '"febre": "",' \
                  '"sudorese": "",' \
                  '"usoAlcool": "",' \
                  '"usoFumo": "",' \
                  '"altApetite": ""}'
    return jsonDefault

class Sistema(models.Model):
    id = models.AutoField(primary_key=True)
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    sintomas = HStoreField(default=jsonfield_default_value())
    # cefaleia = models.CharField(default=None, blank=True, null=True, max_length=55)
    # tonteiras = models.CharField(default=None, blank=True, null=True, max_length=55)
    # convulsoes = models.CharField(default=None, blank=True, null=True, max_length=55)
    # desmaio = models.CharField(default=None, blank=True, null=True, max_length=55)
    # tremor = models.CharField(default=None, blank=True, null=True, max_length=55)
    # difMemoria = models.CharField(default=None, blank=True, null=True, max_length=55)
    # difAudicao = models.CharField(default=None, blank=True, null=True, max_length=55)
    # zumbido = models.CharField(default=None, blank=True, null=True, max_length=55)
    # difConcentracao = models.CharField(default=None, blank=True, null=True, max_length=55)
    # difVisao = models.CharField(default=None, blank=True, null=True, max_length=55)
    # difFalar = models.CharField(default=None, blank=True, null=True, max_length=55)
    # difMastigar = models.CharField(default=None, blank=True, null=True, max_length=55)
    # difPaladar = models.CharField(default=None, blank=True, null=True, max_length=55)
    # difCheiro = models.CharField(default=None, blank=True, null=True, max_length=55)
    # difEngolir = models.CharField(default=None, blank=True, null=True, max_length=55)
    # resfriados = models.CharField(default=None, blank=True, null=True, max_length=55)
    # roquidao = models.CharField(default=None, blank=True, null=True, max_length=55)
    # alergia = models.CharField(default=None, blank=True, null=True, max_length=55)
    # dispneia = models.CharField(default=None, blank=True, null=True, max_length=55)
    # dorToracica = models.CharField(default=None, blank=True, null=True, max_length=55)
    # tosse = models.CharField(default=None, blank=True, null=True, max_length=55)
    # palpitacoes = models.CharField(default=None, blank=True, null=True, max_length=55)
    # edema = models.CharField(default=None, blank=True, null=True, max_length=55)
    # dormencia = models.CharField(default=None, blank=True, null=True, max_length=55)
    # extremidadesFrias = models.CharField(default=None, blank=True, null=True, max_length=55)
    # pirose = models.CharField(default=None, blank=True, null=True, max_length=55)
    # probDigestivo = models.CharField(default=None, blank=True, null=True, max_length=55)
    # nausea = models.CharField(default=None, blank=True, null=True, max_length=55)
    # vomito = models.CharField(default=None, blank=True, null=True, max_length=55)
    # dorAbdominal = models.CharField(default=None, blank=True, null=True, max_length=55)
    # prisaoVentre = models.CharField(default=None, blank=True, null=True, max_length=55)
    # diarreia = models.CharField(default=None, blank=True, null=True, max_length=55)
    # hemorragiaDisgestiva = models.CharField(default=None, blank=True, null=True, max_length=55)
    # constipacao = models.CharField(default=None, blank=True, null=True, max_length=55)
    # incontFecal = models.CharField(default=None, blank=True, null=True, max_length=55)
    # disfagia = models.CharField(default=None, blank=True, null=True, max_length=55)
    # nicturia = models.CharField(default=None, blank=True, null=True, max_length=55)
    # polidipsia = models.CharField(default=None, blank=True, null=True, max_length=55)
    # disuria = models.CharField(default=None, blank=True, null=True, max_length=55)
    # alguria = models.CharField(default=None, blank=True, null=True, max_length=55)
    # urgMiccional = models.CharField(default=None, blank=True, null=True, max_length=55)
    # hematuria = models.CharField(default=None, blank=True, null=True, max_length=55)
    # incontUrinaria = models.CharField(default=None, blank=True, null=True, max_length=55)
    # altJatoUrinario = models.CharField(default=None, blank=True, null=True, max_length=55)
    # retUrinaria = models.CharField(default=None, blank=True, null=True, max_length=55)
    # ativSexual = models.CharField(default=None, blank=True, null=True, max_length=55)
    # corrimento = models.CharField(default=None, blank=True, null=True, max_length=55)
    # pruidoVaginal = models.CharField(default=None, blank=True, null=True, max_length=55)
    # sangramento = models.CharField(default=None, blank=True, null=True, max_length=55)
    # fogacho = models.CharField(default=None, blank=True, null=True, max_length=55)
    # probPele = models.CharField(default=None, blank=True, null=True, max_length=55)
    # dorMuscular = models.CharField(default=None, blank=True, null=True, max_length=55)
    # artralgia = models.CharField(default=None, blank=True, null=True, max_length=55)
    # edemaArticular = models.CharField(default=None, blank=True, null=True, max_length=55)
    # dorColuna = models.CharField(default=None, blank=True, null=True, max_length=55)
    # difMovArticular = models.CharField(default=None, blank=True, null=True, max_length=55)
    # difCaminhar = models.CharField(default=None, blank=True, null=True, max_length=55)
    # queda = models.CharField(default=None, blank=True, null=True, max_length=55)
    # ansiedade = models.CharField(default=None, blank=True, null=True, max_length=55)
    # tristeza = models.CharField(default=None, blank=True, null=True, max_length=55)
    # ideiaMorte = models.CharField(default=None, blank=True, null=True, max_length=55)
    # altSono = models.CharField(default=None, blank=True, null=True, max_length=55)
    # altPeso = models.CharField(default=None, blank=True, null=True, max_length=55)
    # astenia = models.CharField(default=None, blank=True, null=True, max_length=55)
    # febre = models.CharField(default=None, blank=True, null=True, max_length=55)
    # sudorese = models.CharField(default=None, blank=True, null=True, max_length=55)
    # usoAlcool = models.CharField(default=None, blank=True, null=True, max_length=55)
    # usoFumo = models.CharField(default=None, blank=True, null=True, max_length=55)
    # altApetite = models.CharField(default=None, blank=True, null=True, max_length=55)

    class Meta:
        ordering = ["prontuario"]
        verbose_name = "Sistema"
        verbose_name_plural = "Sistemas"