from django import forms
from .models import *
from autenticacao.models import User


class FormConsulta(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'

    paciente = forms.ModelChoiceField(
        queryset=Paciente.objects.all().order_by('nome'),
        widget=forms.HiddenInput(),
        required=False)

    medico = forms.ModelChoiceField(
        queryset=User.objects.all().order_by('nome'),
        widget=forms.HiddenInput(),
        required=False)

    tipo = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}, choices=TIPOS),
        required=True)


class FormObservacoes(forms.ModelForm):
    class Meta:
        model = Observacoes
        fields = '__all__'

    prontuario = forms.CharField(widget=forms.HiddenInput(), required=False)

    queixaPrincipal = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    historiaAtual = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    historiaPregressa = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    historiaFisiologica = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    historiaSocial = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    historiaFamiliar = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    exameFisico = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    avaliacaoFuncional = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    historiaMedicamentosa = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    examesComplementares = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)


class FormHipoteses(forms.ModelForm):
    class Meta:
        model = Hipoteses
        fields = '__all__'

    prontuario = forms.CharField(widget=forms.HiddenInput(), required=False)

    hipotese = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)


class FormPrescricoes(forms.ModelForm):
    class Meta:
        model = Prescricoes
        fields = '__all__'

    prontuario = forms.CharField(widget=forms.HiddenInput(), required=False)

    exameSolicitado = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    condutaTerapeutica = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    medicamentos = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    dieta = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    orientacao = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    encaminhamentos = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)