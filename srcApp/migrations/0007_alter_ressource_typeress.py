# Generated by Django 4.1.1 on 2022-10-08 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srcApp', '0006_alter_ressource_typeress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ressource',
            name='typeRess',
            field=models.CharField(choices=[('Batiment', 'Batiment')], max_length=20),
        ),
    ]