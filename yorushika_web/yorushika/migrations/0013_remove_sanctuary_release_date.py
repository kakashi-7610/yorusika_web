# Generated by Django 3.2.5 on 2022-06-25 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yorushika', '0012_alter_sanctuary_song'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sanctuary',
            name='release_date',
        ),
    ]
