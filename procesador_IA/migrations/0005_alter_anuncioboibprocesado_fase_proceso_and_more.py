# Generated by Django 5.1.5 on 2025-02-26 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("procesador_IA", "0004_anuncioboibprocesado_tipo_personal_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="anuncioboibprocesado",
            name="fase_proceso",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="anuncioboibprocesado",
            name="isla",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="anuncioboibprocesado",
            name="numero_anuncio",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="anuncioboibprocesado",
            name="tipo_personal",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="anuncioboibprocesado",
            name="tipo_proceso",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="anuncioboibprocesado",
            name="tipo_turno",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
