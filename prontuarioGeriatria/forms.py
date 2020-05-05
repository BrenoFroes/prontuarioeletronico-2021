from django import forms
from .models import *


class FormConsulta(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'


class FormProntuario(forms.ModelForm):
    class Meta:
        model = Prontuario
        fields = '__all__'


class FormObservacoes(forms.ModelForm):
    class Meta:
        model = Observacoes
        fields = '__all__'


class FormHipoteses(forms.ModelForm):
    class Meta:
        model = Hipoteses
        fields = '__all__'


class FormPrescricoes(forms.ModelForm):
    class Meta:
        model = Prescricoes
        fields = '__all__'
