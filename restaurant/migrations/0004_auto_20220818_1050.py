# Generated by Django 3.2.15 on 2022-08-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20220816_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='guests',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='lname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
