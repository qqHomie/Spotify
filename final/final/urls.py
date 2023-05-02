"""
URL configuration for final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from spotify.views import (
    ArtistList, ArtistDetail, AlbumList, AlbumDetail,
    SongList, SongDetail, PlaylistList, PlaylistDetail, UserSongList, UserSongDetail,
    UserAlbumList, UserAlbumDetail, UserArtistList, UserArtistDetail, UserView, UserDetail
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', UserView.as_view(), name='user-list'),
    path('api/v1/users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('api/v1/artists/', ArtistList.as_view(), name='artist-list'),
    path('api/v1/artists/<int:pk>/', ArtistDetail.as_view(), name='artist-detail'),
    path('api/v1/albums/', AlbumList.as_view(), name='album-list'),
    path('api/v1/albums/<int:pk>/', AlbumDetail.as_view(), name='album-detail'),
    path('api/v1/songs/', SongList.as_view(), name='song-list'),
    path('api/v1/songs/<int:pk>/', SongDetail.as_view(), name='song-detail'),
    path('api/v1/playlists/', PlaylistList.as_view(), name='playlist-list'),
    path('api/v1/playlists/<int:pk>/', PlaylistDetail.as_view(), name='playlist-detail'),
    path('api/v1/user-songs/', UserSongList.as_view(), name='user-song-list'),
    path('api/v1/user-songs/<int:pk>/', UserSongDetail.as_view(), name='user-song-detail'),
    path('api/v1/user-albums/', UserAlbumList.as_view(), name='user-album-list'),
    path('api/v1/user-albums/<int:pk>/', UserAlbumDetail.as_view(), name='user-album-detail'),
    path('api/v1/user-artists/', UserArtistList.as_view(), name='user-artist-list'),
    path('api/v1/user-artists/<int:pk>/', UserArtistDetail.as_view(), name='user-artist-detail'),
]
