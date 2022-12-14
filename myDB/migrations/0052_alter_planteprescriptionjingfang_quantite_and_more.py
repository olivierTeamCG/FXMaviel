# Generated by Django 4.0.6 on 2022-10-16 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myDB', '0051_alter_planteprescriptionzangfuqui_quantite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planteprescriptionjingfang',
            name='quantite',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='remarques',
            field=models.TextField(blank=True, default='', max_length=2000, null=True, verbose_name='Effets thérapeutiques'),
        ),
    ]
