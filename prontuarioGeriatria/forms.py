from django import forms
from .models import *
from autenticacao.models import User

TRUE_FALSE_CHOICES = (
    (None, '-----'),
    (True, 'Sim'),
    (False, 'Não'),
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
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    historiaAtual = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="História da Doença Atual",
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    exameFisico = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Exame Físico",
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    avaliacaoFuncional = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Avaliação Funcional",
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    historiaMedicamentosa = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="História Medicamentosa / Alergias",
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    examesComplementares = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Exames Complementares Já Existentes",
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)


class FormHipoteses(forms.ModelForm):
    class Meta:
        model = Hipoteses
        fields = '__all__'

    prontuario = forms.CharField(widget=forms.HiddenInput(), required=False)

    hipotese = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Hipóteses Diagnósticas",
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)


class FormPrescricoes(forms.ModelForm):
    class Meta:
        model = Prescricoes
        fields = '__all__'

    prontuario = forms.CharField(widget=forms.HiddenInput(), required=False)

    exameSolicitado = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Exames Solicitados",
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    condutaTerapeutica = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Conduta Terapêutica",
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    medicamentos = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Medicamentos",
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    dieta = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dieta",
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    orientacao = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Orientação Geral",
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    encaminhamentos = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Encaminhamentos Prioritários",
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)


class FormSistema(forms.ModelForm):
    class Meta:
        model = Sistema
        fields = '__all__'

    prontuario = forms.CharField(widget=forms.HiddenInput(), required=False)
    cefaleia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Cefaléia",
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm RangeAll',
                                      'type': 'range',
                                      'id': 'range-filter',
                                      'name': 'points',
                                      'onchange': 'filterme(this.value);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    tonteiras = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Tonteiras",
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm RangeAll',
                                      'type': 'range',
                                      'id': 'range-filter',
                                      'name': 'points',
                                      'onchange': 'filterme(this.value);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    convulsoes = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Convulsões",
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm RangeAll',
                                      'type': 'range',
                                      'id': 'range-filter',
                                      'name': 'points',
                                      'onchange': 'filterme(this.value);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    desmaio = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Desmaio",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    tremor = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Tremor",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    difMemoria = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Dific. Memória",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    difAudicao = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Dific. Audição",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    zumbido = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Zumbido",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    difConcentracao = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Dific. Concentração",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    difVisao = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Dific. Visão",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    difFalar = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Dific. Falar",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    difMastigar = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Dific. Mastigar",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    difPaladar = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Dific. Paladar",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    difCheiro = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Dific. Sentir Cheiro",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    difEngolir = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Dific. Engolir",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    resfriados = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Resfriados Frequentes",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    roquidao = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Roquidão",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    alergia = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Alergia Respiratória",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    dispneia = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Dispnéia",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    dorToracica = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Dor Torácica",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    tosse = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Tosse",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    palpitacoes = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Palpitações",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    edema = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Edema",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    dormencia = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Dormência",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    extremidadesFrias = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Extremidades Frias",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    pirose = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Pirose",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    probDigestivo = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Problema Digestivo",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    nausea = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Náusea",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    vomito = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Vômito",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    dorAbdominal = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Dor Abdominal",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    prisaoVentre = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Prisão de Ventre",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    diarreia = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Diarréia",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    hemorragiaDisgestiva = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Hemorragia Digestiva",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    constipacao = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Constipação Instestinal",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    incontFecal = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Incontin. Fecal",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    disfagia = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Disfagia",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    nicturia = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Nictúria / Poliúria",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    polidipsia = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Polidipsia",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    disuria = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Disúria",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    alguria = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Algúria",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    urgMiccional = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Urg. Miccional",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    hematuria = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Hematúria",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    incontUrinaria = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Incontin. Urinária",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    altJatoUrinario = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Alt. Jato Urinário",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    retUrinaria = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Ret. Urinário",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    ativSexual = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Atividade Sexual",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    corrimento = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Corrimento",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    pruidoVaginal = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Prurido Vaginal",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    sangramento = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Sangramento",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    fogacho = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Fogacho",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    probPele = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Problema de Pele",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    dorMuscular = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Dor Muscular",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    artralgia = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Artralgia",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    edemaArticular = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Edema Articular",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    dorColuna = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Dor Coluna",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    difMovArticular = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Dific. Mov. Articular",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    difCaminhar = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Dific. Caminhar",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    queda = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Queda",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    ansiedade = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Nervos / Ansiedade",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    tristeza = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Tristeza",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    ideiaMorte = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Ideia de Morte",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    altSono = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Alt. Sono",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    altPeso = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Alt. Peso",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    astenia = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Astenia",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    febre = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Febre",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    sudorese = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Sudorese",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    usoAlcool = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Uso Álcool",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    usoFumo = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Uso Fumo",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    altApetite = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        choices=TRUE_FALSE_CHOICES,
        label="Alter. de Apetite",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=False)
