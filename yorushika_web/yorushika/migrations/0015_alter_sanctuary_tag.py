# Generated by Django 3.2.5 on 2022-06-25 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yorushika', '0014_sanctuary_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sanctuary',
            name='tag',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]
