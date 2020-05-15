from django.urls import path
from prontuarioGeriatria import views

app_name = "prontuarioGeriatria"

urlpatterns = [
    path('consulta/<int:paciente_id>', views.cria_consulta, name='consulta'),
    path('observacoes/<int:prontuario_id>/<int:paciente_id>', views.cria_observacoes, name='observacoes'),
    path('hipoteses/<int:prontuario_id>/<int:paciente_id>', views.cria_hipoteses, name='hipoteses'),
    path('prescricoes/<int:prontuario_id>/<int:paciente_id>', views.cria_prescricoes, name='prescricoes'),
    path('historico-consultas/<int:id>', views.exibe_consultas, name='exibe_consultas'),
    path('prontuario/<int:id>', views.exibe_prontuario, name='exibe_prontuario'),
]
