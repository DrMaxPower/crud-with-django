# Generated by Django 3.2.15 on 2022-08-16 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menu'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='booking',
            name='info',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
