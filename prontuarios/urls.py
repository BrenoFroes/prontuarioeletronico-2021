from django.urls import path
from .views import home, pesquisa_pacientes

app_name = "prontuarios"

urlpatterns = [
    path('', home, name='home'),
    path('pacientes/', pesquisa_pacientes, name='exibe_pacientes'),
]
