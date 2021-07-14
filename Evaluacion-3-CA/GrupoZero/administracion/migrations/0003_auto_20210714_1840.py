# Generated by Django 3.2.4 on 2021-07-14 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_alter_usuario_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='contraseña',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='usuario',
        ),
        migrations.AddField(
            model_name='usuario',
            name='contrasena',
            field=models.CharField(default='grupozero', max_length=50, verbose_name='contrasena'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(default='grupozero', max_length=50, primary_key=True, serialize=False, verbose_name='nombre'),
        ),
    ]