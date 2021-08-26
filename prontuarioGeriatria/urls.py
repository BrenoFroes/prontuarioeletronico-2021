from django.urls import path
from prontuarioGeriatria import views

app_name = "prontuarioGeriatria"

urlpatterns = [
    path('consulta/<int:paciente_id>', views.cria_consulta, name='consulta'),


    path('cria-sistema/<int:prontuario_id>/', views.cria_sistema, name='cria-sistema'),
    path('cria-observacoes/<int:prontuario_id>/', views.cria_observacoes, name='cria-observacoes'),
    path('cria-hipoteses/<int:prontuario_id>/', views.cria_hipoteses, name='cria-hipoteses'),
    path('cria-prescricoes/<int:prontuario_id>/', views.cria_prescricoes, name='cria-prescricoes'),

    path('cria-teste-neuro/<int:prontuario_id>/', views.cria_testes, name='cria-teste-neuro'),
    path('cria-teste-neuro/<int:prontuario_id>/', views.cria_testes, name='cria-teste-neuro'),


    path('historico-consultas/<int:paciente_id>', views.exibe_consultas, name='exibe_consultas'),
    path('exibe-prontuario/<int:consulta_id>', views.exibe_prontuario, name='exibe_prontuario'),


    path('prontuario/<int:prontuario_id>/<int:paciente_id>', views.cria_prontuario, name='prontuario'),
    path('finaliza-prontuario/<int:prontuario_id>/', views.finaliza_prontuario, name='finaliza-prontuario'),
]
