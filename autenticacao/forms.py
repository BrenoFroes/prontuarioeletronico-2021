from django import forms
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import User
from prontuarioEletronico import settings

from django.core.mail import send_mail


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.HiddenInput(), required=False)

    # password1 = forms.CharField(label='Password',
    #                             error_messages={'required': 'Campo obrigatório.', },
    #                             widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}))
    #
    # password2 = forms.CharField(label='Password confirmation',
    #                             error_messages={'required': 'Campo obrigatório.', },
    #                             widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}))

    cpf = forms.CharField(error_messages={'required': 'Campo obrigatório.', },
                           widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
                           required=True)

    email = forms.EmailField(error_messages={'required': 'Campo obrigatório.', },
                           widget=forms.EmailInput(attrs={'class': 'form-control form-control-sm'}),
                           required=True)

    nome = forms.CharField(error_messages={'required': 'Campo obrigatório.', },
                           widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
                           required=True)

    crm = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
                           required=False)

    class Meta:
        model = User
        fields = ('email', 'cpf', 'nome', 'crm')

    # def clean_password2(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("As senhas devem ser iguais")
    #     return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        password = User.objects.make_random_password(length=8,
                                                        allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
        print(password)
        user.set_password(password)
        if commit:
            user.save()
            sendEmail(user, password)
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'is_active', 'admin')

    def clean_password(self):
        return self.initial["password"]


def sendEmail(user, password):
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = user.email
    html_content = render_to_string('gerenciamento/passwordEmail.html', {
        'user': user,
        'password': password,
    })
    text_content = strip_tags(html_content)
    send_mail("Bem Vindo ao Prontuário Geriátria UFF", text_content, from_email,
              [to_email], html_message=html_content, fail_silently=True)
