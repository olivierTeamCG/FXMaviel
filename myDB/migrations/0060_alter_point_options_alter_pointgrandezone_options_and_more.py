# Generated by Django 4.0.6 on 2022-12-27 09:59

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myDB', '0059_remove_point_localisationanatomique_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='point',
            options={'verbose_name': 'TUNG - Point'},
        ),
        migrations.AlterModelOptions(
            name='pointgrandezone',
            options={'verbose_name': 'TUNG - Grandes zone'},
        ),
        migrations.AlterModelOptions(
            name='pointzone',
            options={'verbose_name': 'TUNG - Zone'},
        ),
        migrations.RenameField(
            model_name='point',
            old_name='color1',
            new_name='maitreHuColor1',
        ),
        migrations.RenameField(
            model_name='point',
            old_name='color2',
            new_name='maitreHuColor2',
        ),
        migrations.AddField(
            model_name='point',
            name='maitreTungColor1',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None, verbose_name='couleur 1'),
        ),
        migrations.AddField(
            model_name='point',
            name='maitreTungColor2',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None, verbose_name='couleur 2'),
        ),
        migrations.AlterField(
            model_name='point',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Schéma'),
        ),
    ]