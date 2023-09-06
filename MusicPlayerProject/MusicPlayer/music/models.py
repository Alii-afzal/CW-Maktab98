from django.db import models
from account.models import User
from core.models import BaseModel
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(BaseModel):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Artist(BaseModel):
    name = models.CharField(max_length=30)
    bio = models.TextField()
    image = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.name
     
class Song(BaseModel):
    title = models.CharField(max_length=30)
    artists = models.ManyToManyField(Artist)
    cover_photo = models.ImageField(upload_to='song_photos/')
    audio_file = models.FileField(upload_to='audios/')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.title
    
    def get(self):
        for artist in self.artists.all():
            print(artist)
 
class Playlist(BaseModel):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)
    
    def __str__(self):
        return self.title 
    
class Like(BaseModel):
    like_user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_song = models.ForeignKey(Song, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('like_user', 'like_song')  # Ensure a user can like a song only once

    def __str__(self):
        return f'{self.user.username} likes {self.song.title}'
    
class Comment(BaseModel):
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField()
    approve = models.BooleanField(default=False)
    
class RecentlyPlayed(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    played_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  

    def __str__(self):
        return f'{self.user.username} played {self.song.title}'