# Generated by Django 4.1.1 on 2022-10-09 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('srcApp', '0012_rename_account_personnel_compte'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnel',
            name='role',
        ),
    ]