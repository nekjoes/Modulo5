from rest_framework import serializers
from .models import CategoriaJobs
from .models import Trabajo
from .models import ListaTrabajosDisponibles
 


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaJobs
        fields = "__all__"

class TrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajo
        fields = "__all__"

class TrabajoListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaTrabajosDisponibles
        fields = "__all__"