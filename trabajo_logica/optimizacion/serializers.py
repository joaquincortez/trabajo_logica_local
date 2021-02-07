from rest_framework import serializers
from .models import Helado, MateriaPrima, MateriaPrima_Helado

class HeladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Helado
        fields = ('id', 'nombre', 'precio')

class MateriaPrimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MateriaPrima
        fields = ('id', 'nombre', 'costo')

class MateriaPrima_HeladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MateriaPrima_Helado
        fields = ('id', 'helado', 'materia_prima', 'cantidad', 'porcentaje_perdida')

