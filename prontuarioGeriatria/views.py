from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from . models import Observacoes, Hipoteses, Prescricoes
from gerenciamento.models import Paciente
import random


def cria_consulta(request, paciente_id):
    user = request.user
    form = FormConsulta()
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == "POST":
        form = FormConsulta(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.paciente = paciente
            consulta.medico = user
            consulta.save()
            codigo = random.randint(1000, 9999)
            prontuario = Prontuario.objects.create(consulta=consulta, codigo=codigo)
            return redirect('prontuarioGeriatria:revisao_sistema', prontuario_id=prontuario.id, paciente_id=paciente.id)
    return render(request, 'consulta.html', {'form': form, 'pacienteResumo': paciente})


def cria_observacoes(request, prontuario_id, paciente_id):
    form = FormObservacoes()
    paciente = Paciente.objects.get(id=paciente_id)
    prontuario = get_object_or_404(Prontuario, id=prontuario_id)

    if request.method == "GET":
        try:
            obs = Observacoes.objects.get(prontuario=prontuario_id)
            form = FormObservacoes(instance=obs)
        except Observacoes.DoesNotExist:
            form = FormObservacoes()
        return render(request, 'observacoes.html', {'form': form, 'pacienteResumo': paciente, 'prontuario': prontuario})

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
            return redirect('prontuarioGeriatria:hipoteses', prontuario_id=prontuario.id, paciente_id=paciente.id)
    return render(request, 'observacoes.html', {'form': form, 'pacienteResumo': paciente, 'prontuario': prontuario})


def cria_hipoteses(request,  prontuario_id, paciente_id):
    form = FormHipoteses()
    paciente = Paciente.objects.get(id=paciente_id)
    prontuario = get_object_or_404(Prontuario, id=prontuario_id)

    if request.method == "GET":
        try:
            hip = Hipoteses.objects.get(prontuario=prontuario_id)
            form = FormHipoteses(instance=hip)
        except Hipoteses.DoesNotExist:
            form = FormHipoteses()
        return render(request, 'hipoteses.html', {'form': form, 'pacienteResumo': paciente, 'prontuario': prontuario})

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
            return redirect('prontuarioGeriatria:prescricoes', prontuario_id=prontuario.id, paciente_id=paciente.id)
    return render(request, 'hipoteses.html', {'form': form, 'pacienteResumo': paciente, 'prontuario': prontuario})


def cria_prescricoes(request,  prontuario_id, paciente_id):
    form = FormPrescricoes()
    paciente = Paciente.objects.get(id=paciente_id)
    prontuario = get_object_or_404(Prontuario, id=prontuario_id)

    if request.method == "GET":
        try:
            prescricoes = Prescricoes.objects.get(prontuario=prontuario_id)
            form = FormPrescricoes(instance=prescricoes)
        except Prescricoes.DoesNotExist:
            form = FormPrescricoes()
        return render(request, 'prescricoes.html', {'form': form, 'pacienteResumo': paciente, 'prontuario': prontuario})

    if request.method == "POST":
        try:
            prescricoes = Prescricoes.objects.get(prontuario=prontuario_id)
            form = FormPrescricoes(request.POST, instance=prescricoes)
        except Prescricoes.DoesNotExist:
            form = FormPrescricoes(request.POST)

        if form.is_valid():
            prescricoes = form.save(commit=False)
            prescricoes.prontuario = prontuario
            prescricoes.save()
            return redirect('prontuarios:home')
    return render(request, 'prescricoes.html', {'form': form, 'pacienteResumo': paciente, 'prontuario': prontuario})


def exibe_consultas(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    try:
        consultas = Consulta.objects.filter(paciente=id)
    except Consulta.DoesNotExist:
        consultas = []
    return render(request, 'historicoConsultas.html', {'consultas': consultas, 'pacienteResumo': paciente})


def exibe_prontuario(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    try:
        prontuario = Prontuario.objects.get(consulta=id)
    except Prontuario.DoesNotExist:
        return render(request, 'exibeProntuario.html', {'pacienteResumo': consulta.paciente, 'vazio': True})
    return render(request, 'exibeProntuario.html', {'prontuario': prontuario, 'pacienteResumo': consulta.paciente})


def cria_sistema(request, paciente_id, prontuario_id):
    paciente = Paciente.objects.get(id=paciente_id)
    prontuario = get_object_or_404(Prontuario, id=prontuario_id)
    form = FormRevisao()

    if request.method == "GET":
        try:
            sistema = Revisao.objects.get(prontuario=prontuario_id)
            form = FormRevisao(instance=sistema)
        except Revisao.DoesNotExist:
            form = FormRevisao()
        return render(request, 'revisao.html', {'form': form, 'pacienteResumo': paciente, 'prontuario': prontuario})

    if request.method == "POST":
        try:
            sistema = Revisao.objects.get(prontuario=prontuario_id)
            form = FormRevisao(request.POST, instance=sistema)
        except Revisao.DoesNotExist:
            form = FormRevisao(request.POST)

        if form.is_valid():
            sistema = form.save(commit=False)
            sistema.prontuario = prontuario
            sistema.save()
            return redirect('prontuarioGeriatria:observacoes', prontuario_id=prontuario.id, paciente_id=paciente.id)
    return render(request, 'revisao.html', {'form': form, 'pacienteResumo': paciente, 'prontuario': prontuario})

