from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Veiculos, Concessionaria


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class ConcessionariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concessionaria
        fields = '__all__'


class VeiculosSerializer(serializers.ModelSerializer):
    # concessionaria = ConcessionariaSerializer()

    class Meta:
        model = Veiculos
        fields = ['url', 'concessionaria', 'nome', 'cor', 'funciona']


# Modelo não relacional (concessionaria) -> não tem campos que se relacionam com outro modelo
# {
#   'campo1': true
# }

# Modelo relacional (veiculos) -> vai ter algum campo relacionado com outro modelo
# {
#  'campo5': 'nome fulano',
#  'campo10': false,
#  'mod_relaciona': {'campo1': true}
# }