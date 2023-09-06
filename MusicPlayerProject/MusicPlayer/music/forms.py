from django import forms
from music.models import Playlist, Comment, Song


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['title', 'description']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        
class SongUploadForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artists', 'audio_file', 'cover_photo', 'genre']