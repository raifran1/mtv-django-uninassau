from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, VeiculosSerializer, ConcessionariaSerializer
from core.models import Veiculos, Concessionaria


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class VeiculosViewSet(viewsets.ModelViewSet):
    queryset = Veiculos.objects.all()
    serializer_class = VeiculosSerializer


class ConcessionariaViewSet(viewsets.ModelViewSet):
    queryset = Concessionaria.objects.all()
    serializer_class = ConcessionariaSerializer
