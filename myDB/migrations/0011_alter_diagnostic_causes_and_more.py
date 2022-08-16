# Generated by Django 4.0.6 on 2022-08-14 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myDB', '0010_diagnostic_alter_planteprescriptionjingfang_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnostic',
            name='causes',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Causes'),
        ),
        migrations.AlterField(
            model_name='diagnostic',
            name='symptomes_explications',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Symptomes'),
        ),
        migrations.AlterField(
            model_name='diagnostic',
            name='syndrome',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Syndrome'),
        ),
        migrations.AlterField(
            model_name='diagnostic',
            name='syndrome_principal',
            field=models.CharField(blank='', max_length=2000, null=True, verbose_name='Syndrome principal'),
        ),
    ]
