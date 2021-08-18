from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from django import forms
from .models import *
from datetime import datetime
from .choices import *

class FormPessoa(forms.ModelForm):
    anoAtual = datetime.today().year
    mesAtual = datetime.today().month

    class Meta:
        model = Pessoa
        fields = '__all__'

    nome = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=True)

    estadoCivil = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=True,
        choices=ESTADOS_CIVIS_ESCOLHAS)

    naturalidade = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=True)

    nacionalidade = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=True,
        choices=NACIONALIDADES_ESCOLHAS)

    dataNascimento = forms.DateField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.SelectDateWidget(attrs={'class': 'form-control form-control-sm col-lg-3 mr-2 d-inline', 'onclick': 'validatorBorn()'},
                                      years=range(anoAtual, 1899, -1),
                                      empty_label=("Ano", "Mês", "Dia"),),
        required=True)


class FormPaciente(FormPessoa):
    class Meta(FormPessoa.Meta):
        model = Paciente
        fields = '__all__'

    codigo = forms.CharField(widget=forms.HiddenInput(), required=False)

    genero = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=True,
        choices=GENEROS_ESCOLHAS)

    cpf = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=True)

    cns = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    cep = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '9'}),
        required=True)

    endereco = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=True)

    numero = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    complemento = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    tel = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=True)

    escolaridade = forms.ChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=True,
        choices=ESCOLARIDADES_ESCOLHAS)

    profissaoAtual = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        required=False)

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
        for x in ['(', ')', '-', ' ']:
            tel = tel.replace(x, '')
        self.data['tel'] = tel
        return tel


class FormHistorico(forms.ModelForm):
    class Meta:
        model = Historico
        fields = '__all__'

    paciente = forms.CharField(widget=forms.HiddenInput(), required=False)

    historiaPregressa = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        label="História Patológica Pregressa",
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
