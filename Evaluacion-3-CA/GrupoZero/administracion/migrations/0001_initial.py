# Generated by Django 3.2.5 on 2021-07-13 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('usuario', models.IntegerField(primary_key=True, serialize=False, verbose_name='usuario')),
                ('contraseña', models.CharField(max_length=50, verbose_name='contraseña')),
            ],
        ),
    ]
