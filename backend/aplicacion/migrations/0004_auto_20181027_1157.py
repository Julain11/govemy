# Generated by Django 2.1 on 2018-10-27 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_remove_usuario_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='descripcionEstudiante',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='formacion',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='img/fotosapp/'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='curso',
            field=models.IntegerField(default=10),
        ),
    ]
