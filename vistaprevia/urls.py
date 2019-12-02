from django.urls import path
from .views import index, contacto, cargar_imagen
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('', index, name='index'),
        path('contacto/', contacto, name='contacto'),
        path('cargar/', cargar_imagen, name='cargar'),
]
