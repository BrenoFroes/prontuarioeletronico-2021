from django.urls import path
from prontuarioGeriatria import views

app_name = "prontuarioGeriatria"

urlpatterns = [
    path('consulta', views.cria_consulta, name='consulta'),
    path('observacoes/<int:prontuario_id>/<int:paciente_id>', views.cria_observacoes, name='observacoes'),
    path('hipoteses/<int:prontuario_id>/<int:paciente_id>', views.cria_hipoteses, name='hipoteses'),
    path('prescricoes/<int:prontuario_id>/<int:paciente_id>', views.cria_prescricoes, name='prescricoes'),
]
