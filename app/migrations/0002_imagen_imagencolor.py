# Generated by Django 3.2.7 on 2021-09-24 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagen',
            name='imagencolor',
            field=models.ImageField(default='no-imagen.png', null=True, upload_to='', verbose_name='Fotografía a color'),
        ),
    ]
