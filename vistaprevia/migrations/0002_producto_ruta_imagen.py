# Generated by Django 2.2.7 on 2019-11-23 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vistaprevia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='ruta_imagen',
            field=models.FileField(blank=True, default='defecto/defecto.png', null=True, upload_to='fotos/%Y/%m/%d'),
        ),
    ]
