from django.contrib import admin
from .models import Album, Artist, UserAlbum, UserArtist, Playlist, Song, UserSong


# Register your models here.

admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(UserSong)
admin.site.register(UserAlbum)
admin.site.register(UserArtist)
admin.site.register(Playlist)
admin.site.register(Song)
