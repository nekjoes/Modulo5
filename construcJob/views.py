from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view


from construcJob.models import CategoriaJobs, Trabajo, ListaTrabajosDisponibles
from construcJob.serializers import CategoriaSerializer, TrabajoSerializer, TrabajoListaSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo")


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = CategoriaJobs.objects.all()
    serializer_class = CategoriaSerializer
   
class TrabajoViewSet(viewsets.ModelViewSet):
    queryset = Trabajo.objects.all()
    serializer_class = TrabajoSerializer

class LisTrabajoViewSet(viewsets.ModelViewSet):
    queryset = ListaTrabajosDisponibles.objects.all()
    serializer_class = TrabajoListaSerializer



@api_view(["GET"])
def ConterJob(request):
    try:
        cantd = Trabajo.objects.count()
        return JsonResponse({
            "Nº de Trabajos" : cantd
        },
            safe=False,
            status=200,  
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)