# Generated by Django 5.0.3 on 2024-04-13 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kuma', '0005_alter_producto_imagen_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='fecha_vencimiento',
            new_name='fecha_fin_garantía',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='fecha_ingreso',
        ),
    ]
