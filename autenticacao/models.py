from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, cpf, nome, password=None):
        if not email:
            raise ValueError("Usuário precisa ter um e-mail")
        if not password:
            raise ValueError("Usuário precisa ter uma senha")
        if not nome:
            raise ValueError("Usuário precisa ter um nome")
        if not cpf:
            raise ValueError("Usuário precisa ter um cpf")
        user = self.model(
            email=self.normalize_email(email),
            cpf=cpf,
            nome=nome,
        )
        password = BaseUserManager.make_random_password(self, length=8, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
        print(password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, cpf, nome, password=None):
        user = self.create_user(
            email,
            cpf=cpf,
            nome=nome,
            password=password,
        )
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    # email = models.EmailField(unique=True, max_length=55)
    id = models.AutoField(primary_key=True)
    email = models.EmailField(_('e-mail'), unique=True)
    cpf = models.CharField(unique=True, max_length=11)
    nome = models.CharField(max_length=255)
    crm = models.CharField(max_length=55, null=True, blank=True)  # codigo apenas para medicos
    is_active = models.BooleanField(default=True)  # pode se logar
    admin = models.BooleanField(default=False)  # superuser
    medico = models.BooleanField(default=False)  # tipos de usuario
    recepcionista = models.BooleanField(default=False)  # tipos de usuario
    staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cpf', 'nome']

    objects = UserManager()

    def __str__(self):
        return self.nome

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_medico(self):
        return self.medico

    @property
    def is_recepcionista(self):
        return self.recepcionista

    @property
    def is_staff(self):
        return self.staff