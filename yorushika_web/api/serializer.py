from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from yorushika.models import Overview, Album, Song, Recommend, Sanctuary
from django.contrib.auth.models import User


class OverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Overview
        fields = ('id', 'title', 'text', 'image',
                  'created_at', 'display_order')


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('title', 'text', 'image', 'url',
                  'release_date', 'created_at')


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'text', 'url', 'created_at',
                  'album', 'song_order', 'owner', 'highlighted')
        owner = serializers.ReadOnlyField(source='owner.username')


class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommend
        fields = ('id', 'song', 'text', 'created_at', 'user')


class SanctuarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sanctuary
        fields = ('id', 'sanctuary', 'song', 'image',
                  'text', 'tag', 'created_at')


class UserSerializer(serializers.ModelSerializer):
    songs = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Song.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'songs']
