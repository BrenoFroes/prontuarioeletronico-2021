from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import FormPaciente
from .models import Paciente
from autenticacao.forms import UserCreationForm
import random


def cadastra_medico(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.medico = True
            user.save()
            return redirect('prontuarios:home')
    return render(request, 'formMedico.html', {'form': form})


def cadastra_paciente(request):
    form = FormPaciente()
    if request.method == "POST":
        form = FormPaciente(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            codigo = random.randint(100000, 999999)
            paciente.codigo = str(codigo)
            paciente.save()
            messages.add_message(request, messages.INFO, 'Paciente cadastrado com sucesso.')
            print('passei')
            return redirect('prontuarios:home')
        print('form nao é valido')
    return render(request, 'FormPaciente.html', {'form': form, 'acao': 'inclusao'})


def exibe_paciente(request, id):
    if request.method == "GET":
        paciente = get_object_or_404(Paciente, pk=id)
        return render(request, 'pacientePerfil.html', {'paciente': paciente})


def edita_paciente(request, id):
    if request.method == "GET":
        paciente = get_object_or_404(Paciente, pk=id)
        form = FormPaciente(instance=paciente)
        return render(request, 'formPaciente.html', {'form': form, 'acao': 'alteracao'})

    if request.method == "POST":
        paciente = get_object_or_404(Paciente, pk=id)
        form = FormPaciente(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Paciente alterado com sucesso.')
            return redirect('gerenciamento:exibe_paciente', id=paciente.id)
        else:
            return render(request, 'FormPaciente.html', {'form': form, 'acao': 'alteracao'})


def remove_paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    paciente.delete()
    messages.add_message(request, messages.INFO, 'Paciente removido com sucesso.')
    return redirect('prontuarios:home')
