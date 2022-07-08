from django.db import models
from django.contrib.auth.models import User


class Recommend(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=150)
    image = models.ImageField(upload_to='images')
    url = models.URLField(max_length=200, blank=True)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    album = models.CharField(max_length=50)

    def __str__(self):
        return self.title


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

    def __str__(self):
        return self.title


class Sanctuary(models.Model):
    sanctuary = models.CharField(max_length=150)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=True)
    text = models.TextField(max_length=150, blank=True)
    tag = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sanctuary


class Rec(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.song.title
