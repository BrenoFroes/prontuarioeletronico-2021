from django import forms
from .models import Paciente, Medico, Pessoa
from datetime import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class FormPessoa(forms.ModelForm):
    anoAtual = datetime.today().year

    class Meta:
        model = Pessoa
        fields = '__all__'

    consulta_id = forms.CharField(widget=forms.HiddenInput(), required=False)

    nome = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=True)

    estadoCivil = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=True)

    naturalidade = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=True)

    nacionalidade = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=True)

    dataNascimento = forms.DateField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.SelectDateWidget(attrs={'class': 'form-control form-control-sm col-lg-2 d-inline mr-2'},
                                      years=range(1900, anoAtual+1), empty_label=("Ano", "Mês", "Dia"),),
        # widget=DateInput,
        required=False)


class FormPaciente(FormPessoa):
    class Meta(FormPessoa.Meta):
        model = Paciente
        fields = '__all__'

    cep = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=True)

    endereco = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=True)

    tel = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=True)

    profissaoAtual = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=True)

    profissaoAnterior = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    renda = forms.FloatField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
        required=False)


class FormMedico(FormPessoa):
    class Meta:
        model = Medico
        fields = '__all__'

    crm = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=True)

