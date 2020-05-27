from django import forms
from .models import *
from datetime import datetime
from autenticacao.forms import UserCreationForm, UserChangeForm


class FormPessoa(forms.ModelForm):
    anoAtual = datetime.today().year

    class Meta:
        model = Pessoa
        fields = '__all__'

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
                                      years=range(anoAtual, 1899, -1), empty_label=("Ano", "Mês", "Dia"),),
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


class FormMedico(FormPessoa, UserCreationForm):
    class Meta(UserChangeForm.Meta):
        model = Medico
        fields = '__all__'
        exclude = ('password', 'active', 'admin', 'medic', 'recepcionista', 'staff', 'last_login')

    crm = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=True)

