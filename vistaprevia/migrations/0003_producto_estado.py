# Generated by Django 2.2.7 on 2019-11-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vistaprevia', '0002_producto_ruta_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='estado',
            field=models.CharField(choices=[('Borrador', 'Borrador'), ('Publicado', 'Publicado'), ('Retirado', 'Retirado')], default='Borrador', max_length=10),
        ),
    ]
