from django.db import models
from django.conf import settings
from .validators import validarInter, validarJornal
# Create your models here.

class CategoriaJobs(models.Model):
    nombre = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.nombre

class JobsUnits(models.TextChoices):
    Horas = 'Hr', 'Horas'
    Jornal = 'Di', 'Dias'

class Trabajo(models.Model):
    nombre = models.CharField(max_length=100, unique=True) 
    categoria = models.ForeignKey(CategoriaJobs, on_delete=models.CASCADE) 
    description = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=10, validators=[validarInter,validarJornal])
    unidades = models.CharField(
        max_length=2,
        choices=JobsUnits.choices,
        default=JobsUnits.Horas
    )
    disponible = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Trabajo - %s" % self.nombre


class TipoContratista(models.TextChoices):
    Certificado = 'certificado', 'Si Certificado'
    Libre = 'libre', 'Independiente'

class Contratista(models.Model):
    total = models.IntegerField(default=
            0)
    fecha = models.DateField()
    vendedor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="Tipo_de_Empleador"
    )
    estado = models.CharField(
        max_length=20,
        choices=TipoContratista.choices,
        default=TipoContratista.Libre
    )

class ListaTrabajosDisponibles(models.Model):
    Contratista = models.ForeignKey(Contratista, on_delete=models.CASCADE) 
    Trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE) 
    cantidad = models.IntegerField(default=0, validators=[validarInter,])
    Remuneracion = models.DecimalField(decimal_places=2, max_digits=10)