# Generated by Django 4.0.6 on 2023-01-01 21:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myDB', '0068_remove_point_pointzonetung_point_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='localisationAnatomique',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True, verbose_name='Localisation'),
        ),
    ]
