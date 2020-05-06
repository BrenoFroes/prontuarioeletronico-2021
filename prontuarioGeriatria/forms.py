from django import forms
from .models import *


class FormConsulta(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'

        consulta_id = forms.CharField(widget=forms.HiddenInput(), required=False)

        paciente = forms.ModelChoiceField(
            error_messages={'required': 'Campo obrigatório.', },
            queryset=Paciente.objects.all().order_by('nome'),
            empty_label='--- Selecione uma Categoria ---',
            widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
            required=True)

        medico = forms.ModelChoiceField(
            error_messages={'required': 'Campo obrigatório.', },
            queryset=Medico.objects.all().order_by('nome'),
            empty_label='--- Selecione uma Categoria ---',
            widget=forms.Select(attrs={'class': 'form-control form-control-sm',
                                       'size': '80'}),
            required=True)


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
