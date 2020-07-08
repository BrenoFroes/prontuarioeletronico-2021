from django.urls import path
from .views import home, pesquisa_pacientes, minha_conta

app_name = "prontuarios"

urlpatterns = [
    path('', home, name='home'),
    path('pacientes/', pesquisa_pacientes, name='pesquisa_pacientes'),
    path('minha-conta/', minha_conta, name='minha-conta'),
]
