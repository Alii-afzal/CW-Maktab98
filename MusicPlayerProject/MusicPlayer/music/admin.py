from django.contrib import admin
from .models import Genre, Artist, Song, Playlist, Like, Comment

admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(Like)
admin.site.register(Comment)