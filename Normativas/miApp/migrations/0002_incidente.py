# Generated by Django 4.2.2 on 2024-06-15 08:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incidente',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('motivo', models.TextField()),
                ('tipo', models.CharField(max_length=100)),
                ('severidad', models.CharField(choices=[('baja', 'Baja'), ('media', 'Media'), ('alta', 'Alta')], max_length=50)),
                ('equipo_afectado', models.CharField(max_length=200)),
                ('descripcion_equipo_afectado', models.TextField()),
                ('accion_tomada', models.TextField()),
                ('fecha_accion', models.DateTimeField(blank=True, null=True)),
                ('conclusion', models.TextField()),
                ('recomendacion', models.TextField()),
            ],
        ),
    ]