from django.contrib import admin

# Register your models here.

from .models import Consulta, Observacoes, Prontuario, Hipoteses, Prescricoes, Sistema, TestesNeuropsicologicos, TesteComputadorizadoAtencaoVisual

admin.site.register(Consulta)
admin.site.register(Observacoes)
admin.site.register(TestesNeuropsicologicos)
admin.site.register(TesteComputadorizadoAtencaoVisual)
admin.site.register(Prontuario)
admin.site.register(Hipoteses)
admin.site.register(Prescricoes)
admin.site.register(Sistema)