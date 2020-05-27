from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, cpf, nome, password=None):
        if not username:
            raise ValueError("Usuário precisa ter um username")
        if not password:
            raise ValueError("Usuário precisa ter uma senha")
        if not nome:
            raise ValueError("Usuário precisa ter um nome")
        if not cpf:
            raise ValueError("Usuário precisa ter um cpf")
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            cpf=cpf,
            nome=nome,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, cpf, nome, password=None):
        user = self.create_user(
            username,
            email=email,
            cpf=cpf,
            nome=nome,
            password=password,
        )
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=55)
    email = models.EmailField(unique=True, max_length=55)
    cpf = models.CharField(unique=True, max_length=11)
    nome = models.CharField(max_length=255)
    crm = models.CharField(max_length=55, null=True, blank=True)  # codigo apena para medicos
    active = models.BooleanField(default=True)  # pode se logar
    admin = models.BooleanField(default=False)  # superuser
    medico = models.BooleanField(default=False)  # tipos de usuario
    recepcionista = models.BooleanField(default=False)  # tipos de usuario
    staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'cpf', 'nome']

    objects = UserManager()

    def __str__(self):
        return self.nome

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_active(self):
        return self.active

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