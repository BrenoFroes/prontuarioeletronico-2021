from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('prontuarios.urls')),
    path('geriatria/', include('prontuarioGeriatria.urls')),
    path('gerenciamento/', include('gerenciamento.urls')),
    path('autenticacao/', include('autenticacao.urls')),
]
