from django.urls import path
from gerenciamento import views


app_name = "gerenciamento"

urlpatterns = [
    path('cadastro-paciente', views.cadastra_paciente, name='cadastra_paciente'),
    path('cadastro-medico', views.cadastra_medico, name='cadastra_medico'),
]
