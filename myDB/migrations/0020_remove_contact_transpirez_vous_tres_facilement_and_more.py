# Generated by Django 4.0.6 on 2022-08-19 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myDB', '0019_alter_contact_transpirez_vous_tres_facilement_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='transpirez_vous_tres_facilement',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='vous_ne_transpirez_jamais',
        ),
    ]
