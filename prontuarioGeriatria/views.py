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


@user_is_medico
@login_required
def cria_consulta(request, paciente_id):
    user = request.user
    form = FormConsulta()
    paciente = get_object_or_404(Paciente, id=paciente_id)
    inicial = True
    consultas = Consulta.objects.filter(paciente=paciente)
    if len(consultas) > 0:
        inicial = False

    if request.method == "POST":
        form = FormConsulta(request.POST)
        if form.is_valid():
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
    return render(request, 'consulta.html', {'form': form, 'pacienteResumo': paciente, 'inicial': inicial})


@login_required
def exibe_consultas(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    try:
        consultas = Consulta.objects.filter(paciente=paciente_id).order_by('-data')
    except Consulta.DoesNotExist:
        consultas = []
    return render(request, 'historicoConsultas.html', {'consultas': consultas, 'pacienteResumo': paciente})


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
        formSis = FormSistema(instance=sistemas)
    except Sistema.DoesNotExist:
        formSis = FormSistema()

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

    return render(request, 'exibeProntuario.html', {'prontuario': prontuario, 'pacienteResumo': consulta.paciente,
                                                    'formObs': formObs, 'formSis': formSis, 'formHist': formHist,
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

    if sisAnterior:
        sisAnterior = serializers.serialize("python", [sisAnterior, ])
    if obsAnterior:
        obsAnterior = serializers.serialize("python", [obsAnterior, ])
    if hipAnterior:
        hipAnterior = serializers.serialize("python", [hipAnterior, ])
    if prescAnterior:
        prescAnterior = serializers.serialize("python", [prescAnterior, ])

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

    return render(request, 'prontuario.html', {'prontuario': prontuario, 'formObs': formObs, 'formSis': formSis,
                                               'formHip': formHip, 'formPresc': formPresc, 'formHist': formHist,
                                               'pacienteResumo': paciente, 'sisAnterior': sisAnterior,
                                               'obsAnterior': obsAnterior, 'hipAnterior': hipAnterior,
                                               'prescAnterior': prescAnterior})

def changeValues(form):
    _mutable = form.data._mutable
    form.data._mutable = True

    for key, value in form.data.items():
        if value == '0':
            form.data[key] = 'Não informado'
        if value == '-1':
            form.data[key] = '0'

    jsonDefault = '{"cefaleia": "foi",' \
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
    for key, value in jsonObject.items():
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
        elif key == 'difPalar':
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
        elif key == 'hemorragiaDigestiva':
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
        print(form.errors)
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
