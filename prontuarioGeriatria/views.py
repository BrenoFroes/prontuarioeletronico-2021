from django.shortcuts import render
from .forms import *


def criaConsulta(request):
    form = FormConsulta()
    if request.method == "POST":
        form = FormConsulta(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'consulta.html', {'form': form})


def criaProntuario(request):
    form = FormProntuario()
    if request.method == "POST":
        form = FormProntuario(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'prontuario.html', {'form': form})


def criaObservacoes(request):
    form = FormObservacoes()
    if request.method == "POST":
        form = FormObservacoes(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'prontuario.html', {'form': form})


def criaHipoteses(request):
    form = FormHipoteses()
    if request.method == "POST":
        form = FormHipoteses(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'hipoteses.html', {'form': form})


def criaPrescricoes(request):
    form = FormPrescricoes()
    if request.method == "POST":
        form = FormPrescricoes(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'prescricoes.html', {'form': form})