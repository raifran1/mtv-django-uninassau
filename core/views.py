from django.shortcuts import render
from core.models import Veiculos


def index(request):
    veiculos = Veiculos.objects.filter(funciona=True)

    calculo = 7 * 8
    context = {
        'multiplicacao': calculo,
        'veiculos': veiculos,
    }
    return render(request, 'core/index.html', context)
