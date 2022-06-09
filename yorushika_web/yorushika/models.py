from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=150)
    image = models.ImageField(upload_to='images')
    url = models.URLField(max_length=200, blank=True)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Overview(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=250)
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
