from django.urls import path
from prontuarioGeriatria import views

app_name = "prontuarioGeriatria"

urlpatterns = [
    path('consulta', views.cria_consulta, name='consulta'),
    path('prontuario', views.cria_prontuario, name='prontuario'),
    path('observacoes/<int:pk>', views.cria_observacoes, name='observacoes'),
    path('hipoteses/<int:pk>', views.cria_hipoteses, name='hipoteses'),
    path('prescricoes/<int:pk>', views.cria_prescricoes, name='prescricoes'),
]
