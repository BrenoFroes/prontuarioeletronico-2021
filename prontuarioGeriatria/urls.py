from django.urls import path
from prontuarioGeriatria import views

app_name = "prontuarioGeriatria"

urlpatterns = [
    path('consulta', views.criaConsulta, name='consulta'),
    path('prontuario', views.criaProntuario, name='prontuario'),
    path('observacoes', views.criaObservacoes, name='observacoes'),
    path('hipoteses', views.criaHipoteses, name='hipoteses'),
    path('prescricoes', views.criaPrescricoes, name='prescricoes'),
]
