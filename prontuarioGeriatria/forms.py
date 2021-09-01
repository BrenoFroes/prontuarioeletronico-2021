from django.db.models import Model
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import *
from autenticacao.models import User

TRUE_FALSE_CHOICES = (
    (None, '-----'),
    (True, 'Sim'),
    (False, 'Nao'),
)

CDR_CHOICES = (
    (0, '0'),
    (0.5, '0,5'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
)

TMT_CHOICES = (
    (0, '0'),
    (1, '1'),
)

DEP_CHOICES = (
    (0, 'Nao'),
    (1, 'Sim'),
)


class FormConsulta(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'
        exclude = ('data',)

    paciente = forms.ModelChoiceField(
        queryset=Paciente.objects.all().order_by('nome'),
        widget=forms.HiddenInput(),
        required=False)

    medico = forms.ModelChoiceField(
        queryset=User.objects.all().order_by('nome'),
        widget=forms.HiddenInput(),
        required=False)

    tipo = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.HiddenInput(),
        # widget=forms.Select(attrs={'class': 'form-control form-control-sm'}, choices=TIPOS),
        required=False)


class FormObservacoes(forms.ModelForm):
    class Meta:
        model = Observacoes
        fields = '__all__'

    prontuario = forms.CharField(widget=forms.HiddenInput(), required=False)

    queixaPrincipal = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Queixa Principal",
        widget=forms.Textarea(
            attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    historiaAtual = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="História da Doença Atual",
        widget=forms.Textarea(
            attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    exameFisico = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Exame Físico",
        widget=forms.Textarea(
            attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    avaliacaoFuncional = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Avaliação Funcional",
        widget=forms.Textarea(
            attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    historiaMedicamentosa = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="História Medicamentosa / Alergias",
        widget=forms.Textarea(
            attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    examesComplementares = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Exames Complementares Já Existentes",
        widget=forms.Textarea(
            attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)


class FormHipoteses(forms.ModelForm):
    class Meta:
        model = Hipoteses
        fields = '__all__'

    prontuario = forms.CharField(widget=forms.HiddenInput(), required=False)

    hipotese = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Hipóteses Diagnósticas",
        widget=forms.Textarea(
            attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)


class FormTestesNeuropsicologicos(forms.ModelForm):
    class Meta:
        model = TestesNeuropsicologicos
        fields = '__all__'

    prontuario = forms.CharField(widget=forms.HiddenInput(), required=False)

    cdr = forms.IntegerField(
        error_messages={'required': 'Campo obrigatório.', },
        label="CDR",
        widget=forms.Select(
            attrs={'class': 'form-control form-control-sm'}, choices=CDR_CHOICES),
        required=False)

    mmse = forms.IntegerField(
        error_messages={'required': 'Campo obrigatório.',
                        'min_value': 'Mínimo de 0.', 'max_value': 'Máximo de 30.'},
        label="MMSE",
        widget=forms.NumberInput(),
        validators=[MaxValueValidator(30), MinValueValidator(0)],
        required=False)

    vft = forms.IntegerField(
        error_messages={'required': 'Campo obrigatório.',
                        'min_value': 'Mínimo de 0.'},
        label="VFT",
        widget=forms.NumberInput(),
        validators=[MinValueValidator(0)],
        required=False)

    cdt = forms.IntegerField(
        error_messages={'required': 'Campo obrigatório.',
                        'min_value': 'Mínimo de 1.', 'max_value': 'Máximo de 5.'},
        label="CDT",
        widget=forms.NumberInput(),
        validators=[MaxValueValidator(5), MinValueValidator(1)],
        required=False)

    lawton = forms.IntegerField(
        error_messages={'required': 'Campo obrigatório.',
                        'min_value': 'Mínimo de 9.', 'max_value': 'Máximo de 27.'},
        label="LAWTON",
        widget=forms.NumberInput(),
        validators=[MaxValueValidator(27), MinValueValidator(9)],
        required=False)

    depressao = forms.IntegerField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Depressão",
        widget=forms.Select(
            attrs={'class': 'form-control form-control-sm'}, choices=DEP_CHOICES),
        required=False)

    tmt = forms.IntegerField(
        error_messages={'required': 'Campo obrigatório.', },
        label="TMT",
        widget=forms.Select(
            attrs={'class': 'form-control form-control-sm'}, choices=TMT_CHOICES),
        required=False)

    katz = forms.IntegerField(
        error_messages={'required': 'Campo obrigatório.',
                        'min_value': 'Mínimo de 0.', 'max_value': 'Máximo de 6.'},
        label="KATZ",
        widget=forms.NumberInput(),
        validators=[MaxValueValidator(6), MinValueValidator(0)],
        required=False)

    tcaIncorretas = forms.IntegerField(
        error_messages={'required': 'Campo obrigatório.',
                        'min_value': 'Mínimo de 0.', 'max_value': 'Máximo de 100.'},
        label="TCA incorretas (%)",
        widget=forms.NumberInput(),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        required=False)

    tcaOmitidas = forms.IntegerField(
        error_messages={'required': 'Campo obrigatório.',
                        'min_value': 'Mínimo de 0.', 'max_value': 'Máximo de 100.'},
        label="TCA omitidas (%)",
        widget=forms.NumberInput(),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        required=False)

    tcaTempoReacao = forms.IntegerField(
        error_messages={'required': 'Campo obrigatório.',
                        'min_value': 'Mínimo de 0.'},
        label="TCA tempo de reação",
        widget=forms.NumberInput(),
        validators=[MinValueValidator(0)],
        required=False)

    tcaVariabilidadeTempoReacao = forms.IntegerField(
        error_messages={'required': 'Campo obrigatório.',
                        'min_value': 'Mínimo de 0.'},
        label="TCA variabilidade do tempo de reação",
        widget=forms.NumberInput(),
        validators=[MinValueValidator(0)],
        required=False)

    cerad = forms.IntegerField(
        error_messages={'required': 'Campo obrigatório.',
                        'min_value': 'Mínimo de 0.', 'max_value': 'Máximo de 30.'},
        label="CERAD",
        widget=forms.NumberInput(),
        validators=[MaxValueValidator(30), MinValueValidator(0)],
        required=False)


class FormPrescricoes(forms.ModelForm):
    class Meta:
        model = Prescricoes
        fields = '__all__'

    prontuario = forms.CharField(widget=forms.HiddenInput(), required=False)

    exameSolicitado = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Exames Solicitados",
        widget=forms.Textarea(
            attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    condutaTerapeutica = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Conduta Terapêutica",
        widget=forms.Textarea(
            attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    medicamentos = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Medicamentos",
        widget=forms.Textarea(
            attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    dieta = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dieta",
        widget=forms.Textarea(
            attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    orientacao = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Orientação Geral",
        widget=forms.Textarea(
            attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    encaminhamentos = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Encaminhamentos Prioritários",
        widget=forms.Textarea(
            attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)


class FormSistema(forms.ModelForm):
    class Meta:
        model = Sistema
        fields = '__all__'

    sintomas = forms.JSONField(widget=forms.HiddenInput(
        attrs={'style': 'display: none', }
    ),)

    prontuario = forms.CharField(widget=forms.HiddenInput(), required=False)

    cefaleia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Cefaléia",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    tonteiras = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Tonteiras",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    convulsoes = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Convulsões",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    desmaio = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Desmaio",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    tremor = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Tremor",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    difMemoria = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Memória",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    difAudicao = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Audição",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    zumbido = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Zumbido",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    difConcentracao = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Concentração",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    difVisao = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Visão",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    difFalar = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Falar",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    difMastigar = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Mastigar",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    difPaladar = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Paladar",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    difCheiro = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Sentir Cheiro",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    difEngolir = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Engolir",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    resfriados = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Resfriados Frequentes",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    roquidao = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Roquidão",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    alergia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Alergia Respiratória",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    dispneia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dispnéia",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    dorToracica = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dor Torácica",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    tosse = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Tosse",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    palpitacoes = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Palpitações",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    edema = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Edema",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    dormencia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dormência",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    extremidadesFrias = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Extremidades Frias",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    pirose = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Pirose",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    probDigestivo = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Problema Digestivo",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    nausea = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Náusea",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    vomito = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Vômito",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    dorAbdominal = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dor Abdominal",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    prisaoVentre = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Prisão de Ventre",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    diarreia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Diarréia",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    hemorragiaDisgestiva = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Hemorragia Digestiva",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    constipacao = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Constipação Instestinal",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    incontFecal = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Incontin. Fecal",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    disfagia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Disfagia",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    nicturia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Nictúria / Poliúria",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    polidipsia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Polidipsia",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    disuria = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Disúria",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    alguria = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Algúria",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    urgMiccional = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Urg. Miccional",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    hematuria = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Hematúria",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    incontUrinaria = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Incontin. Urinária",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    altJatoUrinario = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Alt. Jato Urinário",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    retUrinaria = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Ret. Urinário",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    ativSexual = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Atividade Sexual",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    corrimento = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Corrimento",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    pruidoVaginal = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Prurido Vaginal",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    sangramento = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Sangramento",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    fogacho = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Fogacho",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    probPele = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Problema de Pele",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    dorMuscular = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dor Muscular",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    artralgia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Artralgia",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    edemaArticular = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Edema Articular",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    dorColuna = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dor Coluna",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    difMovArticular = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Mov. Articular",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    difCaminhar = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Caminhar",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    queda = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Queda",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    ansiedade = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Nervos / Ansiedade",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    tristeza = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Tristeza",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    ideiaMorte = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Ideia de Morte",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    altSono = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Alt. Sono",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    altPeso = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Alt. Peso",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    astenia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Astenia",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    febre = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Febre",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    sudorese = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Sudorese",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    usoAlcool = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Uso Álcool",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    usoFumo = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Uso Fumo",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)

    altApetite = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Alter. de Apetite",
        widget=forms.HiddenInput(
            attrs={'type': 'hidden', 'value': 'Nao informado'}),
        required=False)
