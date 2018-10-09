# Generated by Django 2.1.1 on 2018-10-03 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0007_auto_20181003_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='timeBorrowed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='endTime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='startTime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='timeReturned',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
