from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core import serializers
from django.forms.models import model_to_dict
from .forms import *
from .models import Observacoes, Hipoteses, Prescricoes
from gerenciamento.models import Paciente, Historico
from gerenciamento.forms import FormHistorico
from autenticacao.decorators import user_is_admin, user_is_medico
import json

@user_is_medico
@login_required
def cria_consulta(request, paciente_id):
    user = request.user
    paciente = get_object_or_404(Paciente, id=paciente_id)
    inicial = True
    consultas = Consulta.objects.filter(paciente=paciente)
    if len(consultas) > 0:
        inicial = False

    form = FormConsulta(request.POST)
    consulta = form.save(commit=False)
    if inicial:
        consulta.tipo = "inicial"
    else:
        consulta.tipo = "evolucao"
    consulta.paciente = paciente
    consulta.medico = user
    consulta.save()
    prontuario = Prontuario.objects.create(consulta=consulta)
    return redirect('prontuarioGeriatria:prontuario', prontuario_id=prontuario.id, paciente_id=paciente.id)


@login_required
def exibe_consultas(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    try:
        consultas = Consulta.objects.filter(paciente=paciente_id).order_by('-data')
    except Consulta.DoesNotExist:
        consultas = []
    return render(request, 'historicoConsultas.html', {'consultas': consultas, 'pacienteResumo': paciente})


def deschangeValues(value):
    if value == 'Não informado':
        value = '0'
    return value

def functionFormSistemaJSON(sistemas):
    class FormSistemaJSON(forms.ModelForm):
        class Meta:
            model = Sistema
            fields = '__all__'

        cefaleia = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Cefaléia",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': sistemas.sintomas['cefaleia'],
                                          },
                                   ),
            required=False)

        tonteiras = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Tonteiras",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['tonteiras'])
                                          }
                                   ),
            required=False)

        convulsoes = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Convulsões",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['convulsoes'])
                                          }
                                   ),
            required=False)

        desmaio = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Desmaio",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['desmaio'])
                                          }
                                   ),
            required=False)

        tremor = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Tremor",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['tremor'])
                                          }
                                   ),
            required=False)

        difMemoria = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Dific. Memória",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['difMemoria'])
                                          }
                                   ),
            required=False)

        difAudicao = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Dific. Audição",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['difAudicao'])
                                          }
                                   ),
            required=False)

        zumbido = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Zumbido",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['zumbido'])
                                          }
                                   ),
            required=False)

        difConcentracao = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Dific. Concentração",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['difConcentracao'])
                                          }
                                   ),
            required=False)

        difVisao = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Dific. Visão",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['difVisao'])
                                          }
                                   ),
            required=False)

        difFalar = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Dific. Falar",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['difFalar'])
                                          }
                                   ),
            required=False)

        difMastigar = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Dific. Mastigar",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['difMastigar'])
                                          }
                                   ),
            required=False)

        difPaladar = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Dific. Paladar",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['difPaladar'])
                                          }
                                   ),
            required=False)

        difCheiro = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Dific. Sentir Cheiro",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['difCheiro'])
                                          }
                                   ),
            required=False)

        difEngolir = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Dific. Engolir",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['difEngolir'])
                                          }
                                   ),
            required=False)

        resfriados = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Resfriados Frequentes",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['resfriados'])
                                          }
                                   ),
            required=False)

        roquidao = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Roquidão",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['roquidao'])
                                          }
                                   ),
            required=False)

        alergia = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Alergia Respiratória",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['alergia'])
                                          }
                                   ),
            required=False)

        dispneia = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Dispnéia",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['dispneia'])
                                          }
                                   ),
            required=False)

        dorToracica = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Dor Torácica",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['dorToracica'])
                                          }
                                   ),
            required=False)

        tosse = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Tosse",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['tosse'])
                                          }
                                   ),
            required=False)

        palpitacoes = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Palpitações",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['palpitacoes'])
                                          }
                                   ),
            required=False)

        edema = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Edema",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['edema'])
                                          }
                                   ),
            required=False)

        dormencia = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Dormência",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['dormencia'])
                                          }
                                   ),
            required=False)

        extremidadesFrias = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Extremidades Frias",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['extremidadesFrias'])
                                          }
                                   ),
            required=False)

        pirose = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Pirose",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['pirose'])
                                          }
                                   ),
            required=False)

        probDigestivo = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Problema Digestivo",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['probDigestivo'])
                                          }
                                   ),
            required=False)

        nausea = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Náusea",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['nausea'])
                                          }
                                   ),
            required=False)

        vomito = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Vômito",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['vomito'])
                                          }
                                   ),
            required=False)

        dorAbdominal = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Dor Abdominal",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['dorAbdominal'])
                                          }
                                   ),
            required=False)

        prisaoVentre = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Prisão de Ventre",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['prisaoVentre'])
                                          }
                                   ),
            required=False)

        diarreia = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Diarréia",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['diarreia'])
                                          }
                                   ),
            required=False)

        hemorragiaDisgestiva = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Hemorragia Digestiva",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['hemorragiaDisgestiva'])
                                          }
                                   ),
            required=False)

        constipacao = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Constipação Instestinal",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['constipacao'])
                                          }
                                   ),
            required=False)

        incontFecal = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Incontin. Fecal",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['incontFecal'])
                                          }
                                   ),
            required=False)

        disfagia = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Disfagia",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['disfagia'])
                                          }
                                   ),
            required=False)

        nicturia = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Nictúria / Poliúria",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['nicturia'])
                                          }
                                   ),
            required=False)

        polidipsia = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Polidipsia",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['polidipsia'])
                                          }
                                   ),
            required=False)

        disuria = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Disúria",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['disuria'])
                                          }
                                   ),
            required=False)

        alguria = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Algúria",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['alguria'])
                                          }
                                   ),
            required=False)

        urgMiccional = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Urg. Miccional",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['urgMiccional'])
                                          }
                                   ),
            required=False)

        hematuria = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Hematúria",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['hematuria'])
                                          }
                                   ),
            required=False)

        incontUrinaria = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Incontin. Urinária",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['incontUrinaria'])
                                          }
                                   ),
            required=False)

        altJatoUrinario = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Alt. Jato Urinário",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['altJatoUrinario'])
                                          }
                                   ),
            required=False)

        retUrinaria = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Ret. Urinário",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['retUrinaria'])
                                          }
                                   ),
            required=False)

        ativSexual = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Atividade Sexual",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['ativSexual'])
                                          }
                                   ),
            required=False)

        corrimento = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Corrimento",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['corrimento'])
                                          }
                                   ),
            required=False)

        pruidoVaginal = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Prurido Vaginal",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['pruidoVaginal'])
                                          }
                                   ),
            required=False)

        sangramento = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Sangramento",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['sangramento'])
                                          }
                                   ),
            required=False)

        fogacho = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Fogacho",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['fogacho'])
                                          }
                                   ),
            required=False)

        probPele = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Problema de Pele",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['probPele'])
                                          }
                                   ),
            required=False)

        dorMuscular = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Dor Muscular",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['dorMuscular'])
                                          }
                                   ),
            required=False)

        artralgia = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Artralgia",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['artralgia'])
                                          }
                                   ),
            required=False)

        edemaArticular = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Edema Articular",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['edemaArticular'])
                                          }
                                   ),
            required=False)

        dorColuna = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Dor Coluna",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['dorColuna'])
                                          }
                                   ),
            required=False)

        difMovArticular = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Dific. Mov. Articular",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['difMovArticular'])
                                          }
                                   ),
            required=False)

        difCaminhar = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Dific. Caminhar",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['difCaminhar'])
                                          }
                                   ),
            required=False)

        queda = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Queda",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['queda'])
                                          }
                                   ),
            required=False)

        ansiedade = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Nervos / Ansiedade",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['ansiedade'])
                                          }
                                   ),
            required=False)

        tristeza = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Tristeza",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['tristeza'])
                                          }
                                   ),
            required=False)

        ideiaMorte = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Ideia de Morte",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['ideiaMorte'])
                                          }
                                   ),
            required=False)

        altSono = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Alt. Sono",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['altSono'])
                                          }
                                   ),
            required=False)

        altPeso = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Alt. Peso",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['altPeso'])
                                          }
                                   ),
            required=False)

        astenia = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Astenia",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['astenia'])
                                          }
                                   ),
            required=False)

        febre = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Febre",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['febre'])
                                          }
                                   ),
            required=False)

        sudorese = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Sudorese",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['sudorese'])
                                          }
                                   ),
            required=False)

        usoAlcool = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Uso Álcool",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['usoAlcool'])
                                          }
                                   ),
            required=False)

        usoFumo = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Uso Fumo",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['usoFumo'])
                                          }
                                   ),
            required=False)

        altApetite = forms.CharField(
            error_messages={'required': 'Campo obrigatório.', },
            label="Alter. de Apetite",
            widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm form-check-input indeterminate-check',
                                          'type': 'checkbox',
                                          'value': deschangeValues(sistemas.sintomas['altApetite'])
                                          }
                                   ),
            required=False)
    return FormSistemaJSON

@user_is_medico
@login_required
def exibe_prontuario(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    paciente = consulta.paciente
    try:
        prontuario = Prontuario.objects.get(consulta=consulta_id)
    except Prontuario.DoesNotExist:
        return render(request, 'exibeProntuario.html', {'pacienteResumo': consulta.paciente, 'vazio': True})

    try:
        sistemas = Sistema.objects.get(prontuario=prontuario)
        formSis = functionFormSistemaJSON(sistemas=sistemas)
    except Sistema.DoesNotExist:
        formSis = functionFormSistemaJSON()

    try:
        observacoes = Observacoes.objects.get(prontuario=prontuario)
        formObs = FormObservacoes(instance=observacoes)
    except Observacoes.DoesNotExist:
        formObs = FormObservacoes()

    try:
        prescricoes = Prescricoes.objects.get(prontuario=prontuario)
        formPresc = FormPrescricoes(instance=prescricoes)
    except Prescricoes.DoesNotExist:
        formPresc = FormPrescricoes()

    try:
        hipoteses = Hipoteses.objects.get(prontuario=prontuario)
        formHip = FormHipoteses(instance=hipoteses)
    except Hipoteses.DoesNotExist:
        formHip = FormHipoteses()

    try:
        historico = Historico.objects.get(paciente=paciente)
        formHist = FormHistorico(instance=historico)
    except Historico.DoesNotExist:
        formHist = FormHistorico()

    try:
        testeNeuro = TestesNeuropsicologicos.objects.get(prontuario=prontuario)
        formTesteNeuro = FormTestesNeuropsicologicos(instance=testeNeuro)
    except TestesNeuropsicologicos.DoesNotExist:
        formTesteNeuro = FormTestesNeuropsicologicos()


    return render(request, 'exibeProntuario.html', {'prontuario': prontuario, 'pacienteResumo': consulta.paciente,
                                                    'formObs': formObs, 'formSis': formSis, 'formHist': formHist,
                                                    'formTesteNeuro': formTesteNeuro,
                                                    'formHip': formHip, 'formPresc': formPresc})


@user_is_medico
@login_required
def cria_prontuario(request, prontuario_id, paciente_id):
    prontuario = get_object_or_404(Prontuario, id=prontuario_id)
    paciente = get_object_or_404(Paciente, id=paciente_id)
    consultaAtual = Consulta.objects.get(id=prontuario.consulta_id)

    sisAnterior = None
    obsAnterior = None
    hipAnterior = None
    prescAnterior = None
    testeNeuroAnterior = None

    if consultaAtual.tipo != "inicial":
        consultas = Consulta.objects.filter(paciente=paciente).exclude(id=prontuario.consulta_id).order_by('-data')[:1]
        if consultas:
            try:
                prontuarioAnterior = Prontuario.objects.get(consulta=consultas[0].id)
            except Prontuario.DoesNotExist:
                prontuarioAnterior = None

            if prontuarioAnterior:
                try:
                    sisAnterior = Sistema.objects.get(prontuario=prontuarioAnterior.id)
                except Sistema.DoesNotExist:
                    sisAnterior = None

                try:
                    obsAnterior = Observacoes.objects.get(prontuario=prontuarioAnterior.id)
                except Observacoes.DoesNotExist:
                    obsAnterior = None

                try:
                    hipAnterior = Hipoteses.objects.get(prontuario=prontuarioAnterior.id)
                except Hipoteses.DoesNotExist:
                    hipAnterior = None

                try:
                    prescAnterior = Prescricoes.objects.get(prontuario=prontuarioAnterior.id)
                except Prescricoes.DoesNotExist:
                    prescAnterior = None

                try:
                    testeNeuroAnterior = TestesNeuropsicologicos.objects.get(prontuario=prontuarioAnterior.id)
                except TestesNeuropsicologicos.DoesNotExist:
                    testeNeuroAnterior = None



    if sisAnterior:
        sisAnterior = serializers.serialize("python", [sisAnterior, ])
    if obsAnterior:
        obsAnterior = serializers.serialize("python", [obsAnterior, ])
    if hipAnterior:
        hipAnterior = serializers.serialize("python", [hipAnterior, ])
    if prescAnterior:
        prescAnterior = serializers.serialize("python", [prescAnterior, ])
    if testeNeuroAnterior:
        testeNeuroAnterior = serializers.serialize("python", [testeNeuroAnterior, ])

    try:
        observacoes = Observacoes.objects.get(prontuario=prontuario)
        formObs = FormObservacoes(instance=observacoes)
    except Observacoes.DoesNotExist:
        formObs = FormObservacoes()

    try:
        prescricoes = Prescricoes.objects.get(prontuario=prontuario)
        formPresc = FormPrescricoes(instance=prescricoes)
    except Prescricoes.DoesNotExist:
        formPresc = FormPrescricoes()

    try:
        hipoteses = Hipoteses.objects.get(prontuario=prontuario)
        formHip = FormHipoteses(instance=hipoteses)
    except Hipoteses.DoesNotExist:
        formHip = FormHipoteses()

    try:
        sistemas = Sistema.objects.get(prontuario=prontuario)
        formSis = FormSistema(instance=sistemas)
    except Sistema.DoesNotExist:
        formSis = FormSistema()

    try:
        historico = Historico.objects.get(paciente=paciente)
        formHist = FormHistorico(instance=historico)
    except Historico.DoesNotExist:
        formHist = FormHistorico()

    try:
        testeNeuro = TestesNeuropsicologicos.objects.get(prontuario=prontuario)
        formTesteNeuro = FormTestesNeuropsicologicos(instance=testeNeuro)
    except TestesNeuropsicologicos.DoesNotExist:
        formTesteNeuro = FormTestesNeuropsicologicos()


    return render(request, 'prontuario.html', {'prontuario': prontuario, 'formObs': formObs, 'formSis': formSis,
                                               'formHip': formHip, 'formPresc': formPresc, 'formHist': formHist,
                                               'formTesteNeuro': formTesteNeuro,
                                               'pacienteResumo': paciente, 'sisAnterior': sisAnterior,
                                               'obsAnterior': obsAnterior, 'hipAnterior': hipAnterior,
                                               'prescAnterior': prescAnterior, 'testeNeuroAnterior': testeNeuroAnterior})

def changeValues(form):
    _mutable = form.data._mutable
    form.data._mutable = True

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
    jsonObject = json.loads(jsonDefault)
    for key in jsonObject.items():
        if key == 'cefaleia':
            jsonObject[key] = form.data.get('cefaleia')
        elif key == 'tonteiras':
            jsonObject[key] = form.data.get('tonteiras')
        elif key == 'convulsoes':
            jsonObject[key] = form.data.get('convulsoes')
        elif key == 'desmaio':
            jsonObject[key] = form.data.get('desmaio')
        elif key == 'tremor':
            jsonObject[key] = form.data.get('tremor')
        elif key == 'difMemoria':
            jsonObject[key] = form.data.get('difMemoria')
        elif key == 'difAudicao':
            jsonObject[key] = form.data.get('difAudicao')
        elif key == 'zumbido':
            jsonObject[key] = form.data.get('zumbido')
        elif key == 'difConcentracao':
            jsonObject[key] = form.data.get('difConcentracao')
        elif key == 'difVisao':
            jsonObject[key] = form.data.get('difVisao')
        elif key == 'difFalar':
            jsonObject[key] = form.data.get('difFalar')
        elif key == 'difMastigar':
            jsonObject[key] = form.data.get('difMastigar')
        elif key == 'difPaladar':
            jsonObject[key] = form.data.get('difPaladar')
        elif key == 'difCheiro':
             jsonObject[key] = form.data.get('difCheiro')
        elif key == 'difEngolir':
             jsonObject[key] = form.data.get('difEngolir')
        elif key == 'resfriados':
             jsonObject[key] = form.data.get('resfriados')
        elif key == 'roquidao':
             jsonObject[key] = form.data.get('roquidao')
        elif key == 'alergia':
             jsonObject[key] = form.data.get('alergia')
        elif key == 'dispneia':
             jsonObject[key] = form.data.get('dispneia')
        elif key == 'dorToracica':
             jsonObject[key] = form.data.get('dorToracica')
        elif key == 'tosse':
             jsonObject[key] = form.data.get('tosse')
        elif key == 'palpitacoes':
             jsonObject[key] = form.data.get('palpitacoes')
        elif key == 'edema':
             jsonObject[key] = form.data.get('edema')
        elif key == 'dormencia':
             jsonObject[key] = form.data.get('dormencia')
        elif key == 'extremidadesFrias':
             jsonObject[key] = form.data.get('extremidadesFrias')
        elif key == 'pirose':
             jsonObject[key] = form.data.get('pirose')
        elif key == 'probDigestivo':
             jsonObject[key] = form.data.get('probDigestivo')
        elif key == 'nausea':
             jsonObject[key] = form.data.get('nausea')
        elif key == 'vomito':
             jsonObject[key] = form.data.get('vomito')
        elif key == 'dorAbdominal':
             jsonObject[key] = form.data.get('dorAbdominal')
        elif key == 'prisaoVentre':
             jsonObject[key] = form.data.get('prisaoVentre')
        elif key == 'diarreia':
             jsonObject[key] = form.data.get('diarreia')
        elif key == 'hemorragiaDisgestiva':
             jsonObject[key] = form.data.get('hemorragiaDisgestiva')
        elif key == 'constipacao':
             jsonObject[key] = form.data.get('constipacao')
        elif key == 'incontFecal':
             jsonObject[key] = form.data.get('incontFecal')
        elif key == 'disfagia':
             jsonObject[key] = form.data.get('disfagia')
        elif key == 'nicturia':
             jsonObject[key] = form.data.get('nicturia')
        elif key == 'polidipsia':
             jsonObject[key] = form.data.get('polidipsia')
        elif key == 'disuria':
             jsonObject[key] = form.data.get('disuria')
        elif key == 'alguria':
             jsonObject[key] = form.data.get('alguria')
        elif key == 'urgMiccional':
             jsonObject[key] = form.data.get('urgMiccional')
        elif key == 'hematuria':
             jsonObject[key] = form.data.get('hematuria')
        elif key == 'incontUrinaria':
             jsonObject[key] = form.data.get('incontUrinaria')
        elif key == 'altJatoUrinario':
             jsonObject[key] = form.data.get('altJatoUrinario')
        elif key == 'retUrinaria':
             jsonObject[key] = form.data.get('retUrinaria')
        elif key == 'ativSexual':
             jsonObject[key] = form.data.get('ativSexual')
        elif key == 'corrimento':
             jsonObject[key] = form.data.get('corrimento')
        elif key == 'pruidoVaginal':
             jsonObject[key] = form.data.get('pruidoVaginal')
        elif key == 'sangramento':
             jsonObject[key] = form.data.get('sangramento')
        elif key == 'fogacho':
             jsonObject[key] = form.data.get('fogacho')
        elif key == 'probPele':
             jsonObject[key] = form.data.get('probPele')
        elif key == 'dorMuscular':
            jsonObject[key] = form.data.get('dorMuscular')
        elif key == 'artralgia':
             jsonObject[key] = form.data.get('artralgia')
        elif key == 'edemaArticular':
             jsonObject[key] = form.data.get('edemaArticular')
        elif key == 'dorColuna':
             jsonObject[key] = form.data.get('dorColuna')
        elif key == 'difMovArticular':
             jsonObject[key] = form.data.get('difMovArticular')
        elif key == 'difCaminhar':
             jsonObject[key] = form.data.get('difCaminhar')
        elif key == 'queda':
             jsonObject[key] = form.data.get('queda')
        elif key == 'ansiedade':
             jsonObject[key] = form.data.get('ansiedade')
        elif key == 'tristeza':
             jsonObject[key] = form.data.get('tristeza')
        elif key == 'ideiaMorte':
             jsonObject[key] = form.data.get('ideiaMorte')
        elif key == 'altSono':
             jsonObject[key] = form.data.get('altSono')
        elif key == 'altPeso':
             jsonObject[key] = form.data.get('altPeso')
        elif key == 'astenia':
             jsonObject[key] = form.data.get('astenia')
        elif key == 'febre':
            jsonObject[key] = form.data.get('febre')
        elif key == 'sudorese':
            jsonObject[key] = form.data.get('sudorese')
        elif key == 'usoAlcool':
            jsonObject[key] = form.data.get('usoAlcool')
        elif key == 'usoFumo':
            jsonObject[key] = form.data.get('usoFumo')
        elif key == 'altApetite':
            jsonObject[key] = form.data.get('altApetite')
    form.data['sintomas'] = jsonObject
    form.data._mutable = _mutable
    return form

@user_is_medico
@login_required
def cria_sistema(request, prontuario_id):
    prontuario = get_object_or_404(Prontuario, id=prontuario_id)

    if request.method == "POST":
        try:
            sis = Sistema.objects.get(prontuario=prontuario_id)
            form = FormSistema(request.POST, instance=sis)
        except Sistema.DoesNotExist:
            form = FormSistema(request.POST)

        form = changeValues(form)
        if form.is_valid():
            sistema = form.save(commit=False)
            sistema.prontuario = prontuario
            sistema.sintomas = form.data['sintomas']
            sistema.save()
            obj = model_to_dict(sistema)
            data = {
                'success': True,
                'response': obj
            }
            return JsonResponse(data)
        data = {
            'success': False,
            'error': form.errors
        }
        return JsonResponse(data)


@user_is_medico
@login_required
def cria_observacoes(request, prontuario_id):
    prontuario = get_object_or_404(Prontuario, id=prontuario_id)

    if request.method == "POST":
        try:
            obs = Observacoes.objects.get(prontuario=prontuario_id)
            form = FormObservacoes(request.POST, instance=obs)
        except Observacoes.DoesNotExist:
            form = FormObservacoes(request.POST)

        if form.is_valid():
            observacoes = form.save(commit=False)
            observacoes.prontuario = prontuario
            observacoes.save()
            obj = model_to_dict(observacoes)
            data = {
                'success': True,
                'response': obj
            }
            return JsonResponse(data)
        data = {
            'success': False,
            'error': form.errors
        }
        return JsonResponse(data)

@user_is_medico
@login_required
def cria_testes(request, prontuario_id):
    prontuario = get_object_or_404(Prontuario, id=prontuario_id)
    if request.method == "POST":
        try:
            testeNeuro = TestesNeuropsicologicos.objects.get(prontuario=prontuario_id)
            form = FormTestesNeuropsicologicos(request.POST, instance=testeNeuro)
        except TestesNeuropsicologicos.DoesNotExist:
            form = FormTestesNeuropsicologicos(request.POST)

        if form.is_valid():
            formTesteNeuro = form.save(commit=False)
            formTesteNeuro.prontuario = prontuario
            formTesteNeuro.save()
            obj = model_to_dict(formTesteNeuro)
            data = {
                'success': True,
                'response': obj
            }
            return JsonResponse(data)
        data = {
            'success': False,
            'error': form.errors
        }
        return JsonResponse(data)

@user_is_medico
@login_required
def cria_hipoteses(request, prontuario_id):
    prontuario = get_object_or_404(Prontuario, id=prontuario_id)

    if request.method == "POST":
        try:
            hip = Hipoteses.objects.get(prontuario=prontuario_id)
            form = FormHipoteses(request.POST, instance=hip)
        except Hipoteses.DoesNotExist:
            form = FormHipoteses(request.POST)

        if form.is_valid():
            hipoteses = form.save(commit=False)
            hipoteses.prontuario = prontuario
            hipoteses.save()
            obj = model_to_dict(hipoteses)
            data = {
                'success': True,
                'response': obj
            }
            return JsonResponse(data)
        data = {
            'success': False,
            'error': form.errors
        }
        return JsonResponse(data)


@user_is_medico
@login_required
def cria_prescricoes(request, prontuario_id):
    prontuario = get_object_or_404(Prontuario, id=prontuario_id)

    if request.method == "POST":
        try:
            presc = Prescricoes.objects.get(prontuario=prontuario_id)
            form = FormPrescricoes(request.POST, instance=presc)
        except Prescricoes.DoesNotExist:
            form = FormPrescricoes(request.POST)

        if form.is_valid():
            prescricoes = form.save(commit=False)
            prescricoes.prontuario = prontuario
            prescricoes.save()
            obj = model_to_dict(prescricoes)
            data = {
                'success': True,
                'response': obj
            }
            return JsonResponse(data)
        data = {
            'success': False,
            'error': form.errors
        }
        return JsonResponse(data)


@user_is_medico
@login_required
def finaliza_prontuario(request, prontuario_id):
    prontuario = get_object_or_404(Prontuario, id=prontuario_id)
    prontuario.finalizado = True
    prontuario.save()
    return redirect('prontuarios:home')
