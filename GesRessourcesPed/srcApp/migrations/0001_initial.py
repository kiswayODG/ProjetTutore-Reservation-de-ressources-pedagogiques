# Generated by Django 4.1.1 on 2022-10-01 18:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ressource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeRess', models.CharField(max_length=5)),
                ('typeRess', models.CharField(choices=[('Matériel', 'Matériel')], max_length=10)),
                ('nomRess', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TypePerso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeType', models.CharField(max_length=4)),
                ('fonction', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codePerso', models.CharField(max_length=4)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('dateNaiss', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2004)])),
                ('typePerso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='srcApp.typeperso')),
            ],
        ),
    ]