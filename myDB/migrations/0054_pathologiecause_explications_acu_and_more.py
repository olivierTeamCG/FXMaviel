# Generated by Django 4.0.6 on 2022-11-29 21:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myDB', '0053_alter_plante_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathologiecause',
            name='explications_acu',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Explications'),
        ),
        migrations.AddField(
            model_name='pathologiecause',
            name='explications_pharma',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Explications'),
        ),
        migrations.AlterField(
            model_name='pathologiecause',
            name='explications',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Explications'),
        ),
        migrations.AlterField(
            model_name='pathologiecause',
            name='symptome',
            field=ckeditor.fields.RichTextField(blank='', max_length=2000, null=True, verbose_name='Symptome'),
        ),
        migrations.AlterField(
            model_name='pathologiecause',
            name='traitement_acu',
            field=ckeditor.fields.RichTextField(blank=True, max_length=2000, null=True, verbose_name='Traitement acupuncture'),
        ),
        migrations.AlterField(
            model_name='pathologiecause',
            name='traitement_pharma',
            field=ckeditor.fields.RichTextField(blank=True, max_length=2000, null=True, verbose_name='Traitement pharmacopée'),
        ),
    ]
