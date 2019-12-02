from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from .models import Producto
from .forms import CargaForm


#def index(request):
#   return HttpResponse("Hola Mundo!")

def contacto(request):
    return render(request, 'vistaprevia/contacto.html')

def index(request):
    contenido = {'nombre_sitio' : 'LibrosOnline' }
    para_minorista = {'tipo_usuario' : 'minorista', 'incremento' : '25'}
    para_mayorista = {'tipo_usuario' : 'mayorista', 'incremento' : '10'}
    return render(request, 'vistaprevia/index.html', {'contenido' : contenido,
                                                    'para_minorista' : para_minorista,
                                                    'para_mayorista' : para_mayorista})

def cargar_imagen(request):
    if request.method == 'POST':
        form = CargaForm(request.POST, request.FILES)

        if form.is_valid():
            producto = form.cleaned_data['producto']
            fecha_publicacion = form.cleaned_data['fecha_publicacion']
            ruta_imagen = form.cleaned_data['ruta_imagen']

            newdoc = Producto(producto = producto, fecha_publicacion = fecha_publicacion, ruta_imagen=ruta_imagen)
            newdoc.save()
            return redirect('index')
    else:
        form = CargaForm()
    return render(request, 'vistaprevia/formulario.html', {'form':form})