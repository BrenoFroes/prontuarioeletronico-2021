from django import forms
from .models import Paciente, Medico


class FormPaciente(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'


class FormMedico(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'