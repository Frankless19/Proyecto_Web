# Generated by Django 4.2 on 2023-05-21 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0011_alter_equipo_fechaadquisicion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='nserie',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]