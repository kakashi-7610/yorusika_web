from django.db import models
from django.contrib.auth.models import User
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


class Overview(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=250)
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now=True)
    display_order = models.IntegerField()

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=150)
    image = models.ImageField(upload_to='images')
    url = models.URLField(max_length=200, blank=True)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=150, blank=True)
    url = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_order = models.IntegerField()
    owner = models.ForeignKey(
        'auth.User', related_name='songs', on_delete=models.CASCADE)
    highlighted = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'table': self.title} if self.title else {}
        formatter = HtmlFormatter(
            style=self.style, linenons=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)


class Recommend(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.song.title


class Sanctuary(models.Model):
    sanctuary = models.CharField(max_length=150)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=True)
    text = models.TextField(max_length=150, blank=True)
    tag = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sanctuary
