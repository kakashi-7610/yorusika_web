# Generated by Django 3.2.5 on 2022-06-11 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yorushika', '0005_song_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='recommend_flg',
            field=models.BooleanField(default=False),
        ),
    ]