from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from . import views



router = DefaultRouter()
router.register(r"categoJob", views.CategoriaViewSet)
router.register(r"TrabaJob", views.TrabajoViewSet)
router.register(r"ListaJob", views.LisTrabajoViewSet)

urlpatterns = [
    # path('contacto/<str:nombre>', views.contacto, name='contacto'),
    # path('', views.index, name='index'),
    # path('categorias/', views.categoria, name='categorias'),
    # path('productos/', views.productoFormView, name='productos'),
    # path('mensaje/enviar', views.enviar_mensaje),
    # path('productos/reporte', views.reporte_productos),
    # path('productos/tipo/unidades', views.productos_tipo_unidad),
     path('construcJob/conter', views.ConterJob),
    # path('categorias/create_list', views.CategoriaCreateAndList.as_view(), name='productos'),
     path('', include(router.urls))
]