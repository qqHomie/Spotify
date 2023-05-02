from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Artist, Album, Song, Playlist, UserSong, UserAlbum, UserArtist

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'biography']

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'title', 'release_date', 'artist']

class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(read_only=True)

    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'album']

class PlaylistSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Playlist
        fields = ['id', 'name', 'user', 'songs']

class UserSongSerializer(serializers.ModelSerializer):
    song = SongSerializer(read_only=True)

    class Meta:
        model = UserSong
        fields = ['id', 'user', 'song', 'liked', 'playlist']

class UserAlbumSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(read_only=True)

    class Meta:
        model = UserAlbum
        fields = ['id', 'user', 'album', 'purchased']

class UserArtistSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = UserArtist
        fields = ['id', 'user', 'artist', 'followed']
