# Generated by Django 3.2.4 on 2021-07-12 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_obra_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obra',
            name='imagen',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='core/static/core/img', verbose_name='Imagen'),
        ),
    ]
