from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from gerenciamento.models import Paciente


def pesquisa_pacientes(request):
    query = request.GET.get('buscaPor')
    lista_de_pacientes = Paciente.objects.filter(Q(nome__icontains=query) | Q(codigo=query)).order_by('nome')
    pagina = request.GET.get('pagina', 1)
    paginator = Paginator(lista_de_pacientes, 5)
    try:
        pacientes = paginator.page(pagina)
    except PageNotAnInteger:
        pacientes = paginator.page(1)
    except EmptyPage:
        pacientes = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'pacientes': pacientes, 'buscaPor': query, 'home': False})


@login_required()
def home(request):
    return render(request, 'home.html', {'home': True})
