# Generated by Django 4.0.6 on 2022-08-19 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myDB', '0025_rename_la_pression_le_massage_contact_augmente_douleur_la_pression_le_massage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='LES_COURANTS_DAIR_LE_VENT',
            field=models.BooleanField(default=False, verbose_name="LES COURANTS D'AIR / LE VENT"),
        ),
    ]
