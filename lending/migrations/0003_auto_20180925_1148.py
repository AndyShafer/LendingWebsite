# Generated by Django 2.1.1 on 2018-09-25 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0002_contract'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='borrowedBy',
        ),
        migrations.RemoveField(
            model_name='object',
            name='ownedBy',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
