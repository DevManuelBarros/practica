# Generated by Django 2.2.7 on 2019-11-23 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vistaprevia', '0003_producto_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ManyToManyField(to='vistaprevia.Categoria'),
        ),
    ]
