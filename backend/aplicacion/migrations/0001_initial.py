# Generated by Django 2.1 on 2018-10-08 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('descripcion', models.CharField(max_length=500)),
                ('videos', models.CharField(max_length=200)),
                ('guias', models.FileField(max_length=200, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=200)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(max_length=200)),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Materia')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('num_documento', models.IntegerField(max_length=20)),
                ('correo', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Curso')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Perfil')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='contenido',
            name='contenido_tema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Tema'),
        ),
        migrations.AddField(
            model_name='contenido',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Usuario'),
        ),
    ]