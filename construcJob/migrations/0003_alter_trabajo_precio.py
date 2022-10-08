# Generated by Django 4.1.2 on 2022-10-08 01:28

import construcJob.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construcJob', '0002_contratista_trabajo_listatrabajosdisponibles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajo',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[construcJob.validators.validarInter]),
        ),
    ]