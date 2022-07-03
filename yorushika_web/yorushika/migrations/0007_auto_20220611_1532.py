# Generated by Django 3.2.5 on 2022-06-11 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yorushika', '0006_song_recommend_flg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField(max_length=150)),
                ('image', models.ImageField(upload_to='images')),
                ('url', models.URLField(blank=True)),
                ('release_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField(max_length=150)),
                ('image', models.ImageField(upload_to='images')),
                ('url', models.URLField(blank=True)),
                ('release_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('album', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]