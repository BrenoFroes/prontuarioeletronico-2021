from django.shortcuts import render, redirect
from .forms import FormMedico, FormPaciente


def cadastra_medico(request):
    form = FormMedico()
    if request.method == "POST":
        form = FormMedico(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prontuarios:home')
    return render(request, 'formMedico.html', {'form': form})


def cadastra_paciente(request):
    form = FormPaciente()
    if request.method == "POST":
        form = FormPaciente(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prontuarios:home')
    return render(request, 'FormPaciente.html', {'form': form})
