# Generated by Django 4.0.6 on 2022-09-05 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myDB', '0040_contactfrancois'),
    ]

    operations = [
        migrations.CreateModel(
            name='Symptome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptome', models.CharField(blank='', max_length=200, null=True, verbose_name='symptome')),
            ],
        ),
        migrations.AlterModelOptions(
            name='contactfrancois',
            options={'verbose_name': 'Contact François', 'verbose_name_plural': 'Contacts François'},
        ),
        migrations.AlterModelOptions(
            name='contactfx',
            options={'verbose_name': 'Contact FX', 'verbose_name_plural': 'Contacts FX'},
        ),
        migrations.CreateModel(
            name='SymptomeCause',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('explications', models.TextField(blank=True, max_length=5000, null=True, verbose_name='Eexplications')),
                ('traitement_acu', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Traitement acupuncture')),
                ('traitement_pharma', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Traitement pharmacopée')),
                ('symptome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myDB.symptome')),
            ],
            options={
                'verbose_name': 'Cause',
            },
        ),
    ]