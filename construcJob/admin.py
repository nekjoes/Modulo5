from inspect import trace
from django.contrib import admin
from .models import CategoriaJobs
from .models import Trabajo
from .models import Contratista
from .models import ListaTrabajosDisponibles

admin.site.register(CategoriaJobs)
admin.site.register(Trabajo)
admin.site.register(Contratista)
admin.site.register(ListaTrabajosDisponibles)
# Register your models here.
