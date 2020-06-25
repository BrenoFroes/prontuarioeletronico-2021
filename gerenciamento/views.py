from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .forms import FormPaciente, FormHistorico
from .models import Paciente, Historico
from autenticacao.forms import UserCreationForm
from autenticacao.models import User
import random
from prontuarioEletronico import settings

from django.core.mail import send_mail





@login_required
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
            return redirect('prontuarios:home')
        print(form.errors)
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


def cria_historico(request, id):
    paciente = get_object_or_404(Paciente, pk=id)

    if request.method == "POST":
        # try:
        #     data = {
        #         'sucess': False,
        #         'error': 'Paciente não pode ter mais de um Histórico'
        #     }
        #     return JsonResponse(data)
        #
        # except Historico.DoesNotExist:
        #     form = FormHistorico(request.POST)

        try:
            historico = Historico.objects.get(paciente=paciente)
            form = FormHistorico(request.POST, instance=historico)
        except Historico.DoesNotExist:
            form = FormHistorico(request.POST)

        if form.is_valid():
            historico = form.save(commit=False)
            historico.paciente = paciente
            historico.save()
            obj = model_to_dict(historico)
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


def edita_historico(request, id):
    paciente = get_object_or_404(Paciente, pk=id)

    if request.method == "POST":
        try:
            historico = Historico.objects.get(paciente=paciente)
            form = FormHistorico(request.POST, instance=historico)
        except Historico.DoesNotExist:
            form = FormHistorico(request.POST)

        if form.is_valid():
            historico = form.save(commit=False)
            historico.paciente = paciente
            historico.save()
            obj = model_to_dict(historico)
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
