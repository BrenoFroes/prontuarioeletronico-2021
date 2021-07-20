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
            form.data[key] = 'Vazio'
        if value == '-1':
            form.data[key] = '0'

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
