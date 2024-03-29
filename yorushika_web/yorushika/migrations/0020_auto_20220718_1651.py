# Generated by Django 3.2.5 on 2022-07-18 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yorushika', '0019_auto_20220705_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommend',
            name='album',
        ),
        migrations.RemoveField(
            model_name='recommend',
            name='image',
        ),
        migrations.RemoveField(
            model_name='recommend',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='recommend',
            name='title',
        ),
        migrations.RemoveField(
            model_name='recommend',
            name='url',
        ),
        migrations.AddField(
            model_name='recommend',
            name='song',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='yorushika.song'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recommend',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recommend',
            name='text',
            field=models.TextField(max_length=300),
        ),
        migrations.DeleteModel(
            name='Rec',
        ),
    ]
