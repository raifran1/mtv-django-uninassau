from django.shortcuts import render
from core.models import Veiculos, Concessionaria


def index(request):
    veiculos = Veiculos.objects.filter(funciona=True)
    context = {
        'veiculos': veiculos,
    }
    return render(request, 'core/index.html', context)


def concessionaria(request):
    concessionarias = Concessionaria.objects.filter(funcionando=True)
    context = {
        'concessionarias': concessionarias,
    }
    return render(request, 'core/concessionaria.html', context)