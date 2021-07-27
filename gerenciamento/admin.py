from django.contrib import admin
from .models import Paciente, Historico

admin.site.register(Paciente)
admin.site.register(Historico)