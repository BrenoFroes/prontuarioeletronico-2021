from django.urls import path
from gerenciamento import views

app_name = "gerenciamento"

urlpatterns = [
    path('cadastro-paciente', views.cadastra_paciente, name='cadastra_paciente'),
    path('cadastro-medico', views.cadastra_medico, name='cadastra_medico'),
    path('paciente/<int:id>', views.exibe_paciente, name='exibe_paciente'),
    path('paciente/edit/<int:id>', views.edita_paciente, name='edita_paciente'),
    path('paciente/delete/<int:id>', views.remove_paciente, name='remove_paciente'),
]
