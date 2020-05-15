from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from . models import Observacoes, Hipoteses, Prescricoes
import random


def cria_consulta(request):
    form = FormConsulta()
    if request.method == "POST":
        form = FormConsulta(request.POST)
        if form.is_valid():
            consulta = form.save()
            codigo = random.randint(1000, 9999)
            prontuario = Prontuario.objects.create(consulta=consulta, codigo=codigo)
            paciente = consulta.paciente
            return redirect('prontuarioGeriatria:observacoes', prontuario_id=prontuario.id, paciente_id=paciente.id)
    return render(request, 'consulta.html', {'form': form})


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
    except:
        return render(request, 'exibeProntuario.html', {'pacienteResumo': consulta.paciente, 'vazio': True})
    return render(request, 'exibeProntuario.html', {'prontuario': prontuario, 'pacienteResumo': consulta.paciente})
