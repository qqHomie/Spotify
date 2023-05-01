from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song, related_name='playlists')

    def __str__(self):
        return self.name


class UserSong(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user


class UserAlbum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.user


class UserArtist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    followed = models.BooleanField(default=False)

    def __str__(self):
        return self.user