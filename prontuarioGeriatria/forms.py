import json

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

    sintomas = forms.JSONField(widget=forms.HiddenInput(
                                    attrs={'style': 'display: none',
                                           }
                                    ),
                                )
    prontuario = forms.CharField(widget=forms.HiddenInput(), required=False)
    cefaleia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Cefaléia",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    tonteiras = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Tonteiras",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    convulsoes = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Convulsões",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    desmaio = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Desmaio",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    tremor = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Tremor",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    difMemoria = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Memória",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    difAudicao = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Audição",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    zumbido = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Zumbido",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    difConcentracao = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Concentração",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    difVisao = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Visão",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    difFalar = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Falar",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    difMastigar = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Mastigar",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    difPaladar = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Paladar",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    difCheiro = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Sentir Cheiro",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    difEngolir = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Engolir",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    resfriados = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Resfriados Frequentes",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    roquidao = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Roquidão",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    alergia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Alergia Respiratória",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    dispneia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dispnéia",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    dorToracica = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dor Torácica",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    tosse = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Tosse",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    palpitacoes = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Palpitações",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    edema = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Edema",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    dormencia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dormência",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    extremidadesFrias = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Extremidades Frias",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    pirose = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Pirose",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    probDigestivo = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Problema Digestivo",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    nausea = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Náusea",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    vomito = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Vômito",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    dorAbdominal = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dor Abdominal",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    prisaoVentre = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Prisão de Ventre",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    diarreia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Diarréia",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    hemorragiaDisgestiva = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Hemorragia Digestiva",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    constipacao = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Constipação Instestinal",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    incontFecal = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Incontin. Fecal",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    disfagia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Disfagia",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    nicturia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Nictúria / Poliúria",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    polidipsia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Polidipsia",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    disuria = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Disúria",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    alguria = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Algúria",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    urgMiccional = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Urg. Miccional",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    hematuria = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Hematúria",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    incontUrinaria = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Incontin. Urinária",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    altJatoUrinario = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Alt. Jato Urinário",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    retUrinaria = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Ret. Urinário",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    ativSexual = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Atividade Sexual",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    corrimento = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Corrimento",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    pruidoVaginal = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Prurido Vaginal",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    sangramento = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Sangramento",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    fogacho = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Fogacho",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    probPele = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Problema de Pele",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    dorMuscular = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dor Muscular",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    artralgia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Artralgia",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    edemaArticular = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Edema Articular",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    dorColuna = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dor Coluna",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    difMovArticular = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Mov. Articular",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    difCaminhar = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Dific. Caminhar",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    queda = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Queda",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    ansiedade = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Nervos / Ansiedade",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    tristeza = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Tristeza",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    ideiaMorte = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Ideia de Morte",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    altSono = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Alt. Sono",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    altPeso = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Alt. Peso",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    astenia = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Astenia",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    febre = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Febre",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    sudorese = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Sudorese",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    usoAlcool = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Uso Álcool",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    usoFumo = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Uso Fumo",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)

    altApetite = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="Alter. de Apetite",
        widget=forms.TextInput(attrs={'class': 'form-range range-all',
                                      'type': 'range',
                                      'name': 'points',
                                      'onchange': 'changeRange(this);',
                                      'min': '-1',
                                      'max': '1',
                                      'value': '0',
                                      }
                               ),
        required=False)
