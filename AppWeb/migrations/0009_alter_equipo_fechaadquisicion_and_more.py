# Generated by Django 4.2 on 2023-05-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0008_alter_empleado_dni_alter_equipo_nserie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='fechaAdquisicion',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='fechaPuestaMarcha',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='fechaApertura',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='fechaResolucion',
            field=models.DateField(blank=True),
        ),
    ]
