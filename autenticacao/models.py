from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Usuário precisa ter um cpf")
        if not password:
            raise ValueError("Usuário precisa ter uma senha")
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
        )
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=11)
    active = models.BooleanField(default=True)  # pode se logar
    admin = models.BooleanField(default=False)  # superuser
    medic = models.BooleanField(default=False)  # tipos de usuario
    recepcionista = models.BooleanField(default=False)  # tipos de usuario
    staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

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
        return self.medic

    @property
    def is_recepcionista(self):
        return self.recepcionista

    @property
    def is_staff(self):
        return self.staff