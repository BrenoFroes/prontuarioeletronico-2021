from django.urls import path
from .views import home

app_name = "prontuarios"

urlpatterns = [
    path('', home, name='home')
]
