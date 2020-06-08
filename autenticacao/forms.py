from django import forms
from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',
                                error_messages={'required': 'Campo obrigatório.', },
                                widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}))

    password2 = forms.CharField(label='Password confirmation',
                                error_messages={'required': 'Campo obrigatório.', },
                                widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}))

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

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas devem ser iguais")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        return self.initial["password"]
