# Generated by Django 3.2.15 on 2022-08-19 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_auto_20220819_1355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['type', 'price']},
        ),
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
