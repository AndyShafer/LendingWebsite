# Generated by Django 2.1.1 on 2018-10-09 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0009_auto_20181003_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='endTime',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='lateFee',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contract',
            name='rentalPrice',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contract',
            name='startTime',
            field=models.DateField(blank=True, null=True),
        ),
    ]
