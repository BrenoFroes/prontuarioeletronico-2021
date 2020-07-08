from django import forms
from django.core.exceptions import ValidationError

from .models import *
from datetime import datetime


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

    codigo = forms.CharField(widget=forms.HiddenInput(), required=False)

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

    def clean_phone(self):
        phone = self.data['tel']
        tel = phone
        print('dentro: ', tel)
        for x in ['(', ')', '-', ' ']:
            tel = tel.replace(x, '')
        print('dentro: ', tel)
        self.data['tel'] = tel
        return tel


class FormHistorico(forms.ModelForm):
    class Meta:
        model = Historico
        fields = '__all__'

    paciente = forms.CharField(widget=forms.HiddenInput(), required=False)

    historiaPregressa = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="História Patológica Pregrassa",
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    historiaFisiologica = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="História Fisiológica",
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    historiaSocial = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="História Social / Econômica",
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)

    historiaFamiliar = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="História Patológica Familiar",
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
        required=True)
