from django.shortcuts import render
from .forms import FormMedico, FormPaciente


def cadastra_medico(request):
    form = FormMedico()
    if request.method == "POST":
        form = FormMedico(request.POST)
        if form.is_valid():
            print(form)
            form.save()
    return render(request, 'formMedico.html', {'form': form})


def cadastra_paciente(request):
    form = FormPaciente()
    if request.method == "POST":
        form = FormPaciente(request.POST)
        if form.is_valid():
            print(form)
            form.save()
    return render(request, 'FormPaciente.html', {'form': form})