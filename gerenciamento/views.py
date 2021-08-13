from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .forms import FormPaciente, FormHistorico
from .models import Paciente, Historico
from autenticacao.forms import UserCreationForm
from autenticacao.decorators import user_is_admin, user_is_medico
import random
from datetime import datetime

@user_is_admin
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
    return render(request, 'gerenciamento/users-form.html', {'form': form})


@user_is_admin
@login_required
def cadastra_recepcionista(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.recepcionista = True
            user.save()
            return redirect('prontuarios:home')
    return render(request, 'gerenciamento/users-form.html', {'form': form})


@login_required
def cadastra_paciente(request):
    form = FormPaciente()
    if request.method == "POST":
        form = FormPaciente(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            # Gera o código do paciente baseado em: 2 algoritmos aleatorios + 2 algoritmos de segundo + 2 algoritmos de mes + 2 algoritmos de mes
            codigo = random.randint(10, 99)
            codigo = datetime.today().strftime('%d%m') + datetime.today().strftime('%S') + str(codigo)
            paciente.codigo = codigo
            paciente.save()
            messages.add_message(request, messages.INFO, 'Paciente cadastrado com sucesso.')
            return redirect('prontuarios:home')
    return render(request, 'gerenciamento/formPaciente.html', {'form': form, 'acao': 'inclusao'})


@login_required
def exibe_paciente(request, id):
    if request.method == "GET":
        paciente = get_object_or_404(Paciente, pk=id)
        return render(request, 'gerenciamento/pacientePerfil.html', {'paciente': paciente})


@login_required
def edita_paciente(request, id):
    if request.method == "GET":
        paciente = get_object_or_404(Paciente, pk=id)
        form = FormPaciente(instance=paciente)
        return render(request, 'gerenciamento/formPaciente.html', {'form': form, 'acao': 'alteracao'})

    if request.method == "POST":
        paciente = get_object_or_404(Paciente, pk=id)
        codigo = paciente.codigo
        form = FormPaciente(request.POST, instance=paciente)
        # form.clean_phone()
        if form.is_valid():
            p = form.save(commit=False)
            p.codigo = codigo
            p.save()
            messages.add_message(request, messages.INFO, 'Paciente alterado com sucesso.')
            return redirect('gerenciamento:exibe_paciente', id=paciente.id)
        else:
            return render(request, 'gerenciamento/formPaciente.html', {'form': form, 'acao': 'alteracao'})


@login_required
def remove_paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    paciente.delete()
    messages.add_message(request, messages.INFO, 'Paciente removido com sucesso.')
    return redirect('prontuarios:home')


@user_is_medico
@login_required
def cria_historico(request, id):
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


@user_is_medico
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
