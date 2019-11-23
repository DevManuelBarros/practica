from django.db import models

class Producto(models.Model):
    Borrador = 'Borrador'
    Publicado = 'Publicado'
    Retirado = 'Retirado'
    APROBACION_PRODUCTO = (
        (Borrador, 'Borrador'),
        (Publicado, 'Publicado'),
        (Retirado, 'Retirado'),
    )
    producto = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField("Fecha de Publicación")
    ruta_imagen = models.FileField(upload_to='fotos/%Y/%m/%d', default='defecto/defecto.png', blank=True, null=True)
    estado = models.CharField(max_length=10, choices=APROBACION_PRODUCTO, default='Borrador')

    def __str__(self):
        return ('<%s => %s: %s, %s>' % (self.__class__.__name__, self.producto, self.fecha_publicacion, self.ruta_imagen))

