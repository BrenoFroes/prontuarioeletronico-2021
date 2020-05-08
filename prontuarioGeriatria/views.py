from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
import random

def cria_consulta(request):
    form = FormConsulta()
    if request.method == "POST":
        form = FormConsulta(request.POST)
        if form.is_valid():
            consulta = form.save()
            codigo = random.randint(1000, 9999)
            print(codigo)
            prontuario = Prontuario.objects.create(consulta=consulta, codigo=codigo)
            return redirect('prontuarioGeriatria:observacoes', pk=prontuario.id)
    return render(request, 'consulta.html', {'form': form})


def cria_prontuario(request):
    form = FormProntuario()
    if request.method == "POST":
        form = FormProntuario(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'prontuario.html', {'form': form})


def cria_observacoes(request, pk):
    form = FormObservacoes()
    if request.method == "POST":
        # prontuario = Prontuario.objects.get(id=pk)
        prontuario = get_object_or_404(Prontuario, id=pk)
        form = FormObservacoes(request.POST)
        if form.is_valid():
            observacoes = form.save(commit=False)
            observacoes.prontuario = prontuario
            observacoes.save()
            return redirect('prontuarioGeriatria:hipoteses', pk=prontuario.id)
    return render(request, 'observacoes.html', {'form': form})


def cria_hipoteses(request, pk):
    form = FormHipoteses()
    if request.method == "POST":
        form = FormHipoteses(request.POST)
        prontuario = get_object_or_404(Prontuario, id=pk)
        if form.is_valid():
            hipoteses = form.save(commit=False)
            hipoteses.prontuario = prontuario
            hipoteses.save()
            return redirect('prontuarioGeriatria:prescricoes', pk=prontuario.id)
    return render(request, 'hipoteses.html', {'form': form})


def cria_prescricoes(request, pk):
    form = FormPrescricoes()
    if request.method == "POST":
        form = FormPrescricoes(request.POST)
        prontuario = get_object_or_404(Prontuario, id=pk)
        if form.is_valid():
            prescricoes = form.save(commit=False)
            prescricoes.prontuario = prontuario
            prescricoes.save()
            return redirect('prontuarios:home')
    return render(request, 'prescricoes.html', {'form': form})
