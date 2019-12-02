from django.forms import ModelForm
from .models import Producto

class CargaForm(ModelForm):
    class Meta:
        model = Producto
        fields = ('categoria', 'producto', 'fecha_publicacion', 'ruta_imagen')

        error_messages = {
            'producto' : {
                'required' : ('Se debe agregar un nombre de producto')
            },
            'fecha_publicacion' : {
                'required': ('Se debe agregar la fecha de publicación en el formato adecuado')
            },
        }
    def __init__(self, *args, **kwargs):
        super(CargaForm, self).__init__(*args, **kwargs)