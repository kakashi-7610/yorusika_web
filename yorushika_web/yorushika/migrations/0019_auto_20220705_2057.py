# Generated by Django 3.2.5 on 2022-07-05 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yorushika', '0018_rec'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rec',
            name='title',
        ),
        migrations.AlterField(
            model_name='rec',
            name='text',
            field=models.TextField(max_length=300),
        ),
    ]
