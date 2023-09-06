from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from music.models import Song, Playlist, User, Like, Comment
from music.forms import PlaylistForm, CommentForm


def home(request):
    return render(request, 'index.html')

class SongListView(ListView):
    model = Song
    template_name = 'song_list.html'
    context_object_name = 'songs'
    
class SongDetailView(DetailView):
    model = Song
    template_name = 'song_detail.html'
    context_object_name = 'song'
    
def create_playlist(request):
    if request.user.is_authenticated and request.user and request.user.account_type == 'VIP' and request.user == Playlist.owner:
        if request.method == 'POST':
            form = PlaylistForm(request.POST)
            if form.is_valid():
                playlist = form.save(commit=False)
                playlist.owner = request.user
                playlist.save()
                return redirect('playlist_detail', playlist_id = playlist.id)
        else:
            form = PlaylistForm()
        return render(request, 'create_playlist.html', {'form':form})
    else:
        return render(request, 'permission_denied.html') 
        # raise ValidationError("you don't correctly authenticated")
        
def edit_playlist(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    if request.user.is_authenticated and request.user.account_type == 'VIP' and request.user == playlist.owner:
        if request.method == 'POST':
            form = PlaylistForm(request.POST, instance=playlist)
            if form.is_valid():
                playlist = form.save()
                return redirect('playlist_detail', playlist_id=playlist.id)
        else:
            form = PlaylistForm(instance=playlist)
        return render(request, 'edit_playlist.html', {'form': form, 'playlist': playlist})
    else:
        return render(request, 'permission_denied.html')  


def delete_playlist(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    if request.user.is_authenticated and request.user.account_type == 'VIP' and request.user == playlist.owner:
        if request.method == 'POST':
            playlist.delete()
            return redirect('playlist_list')
        return render(request, 'delete_playlist.html', {'playlist': playlist})
    else:
        return render(request, 'permission_denied.html')


def play_playlist(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    songs = playlist.songs.all()
    return render(request, 'play_playlist.html', {'playlist': playlist, 'songs': songs})

def like_song(request, song_id):
    if request.user.is_authenticated:
        song = get_object_or_404(Song, id=song_id)
        like, created = Like.objects.get_or_create(user=request.user, song=song)
        if not created:
            like.delete()
        return redirect('song_detail', song_id=song_id)
    else:
        return redirect('login')
    
def liked_songs(request):
    if request.user.is_authenticated:
        liked_songs = Like.objects.filter(user=request.user).values('song')
        songs = Song.objects.filter(id__in=liked_songs)
        return render(request, 'liked_songs.html', {'songs': songs})
    else:
        return redirect('login')
    
def comment_song(request, song_id):
    if request.user.is_authenticated:
        song = get_object_or_404(Song, id=dong_id)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.song = song
                comment.save()
                return redirect('song_detail', song_id=song_id)
        else:
            form = CommentForm()
        return render(request, 'comment_song.html', {'form':form, 'song':song})
    else:
        return redirect('login')
    
def user_profile(request):
    if request.user.is_authenticated:
        liked_songs = Like.objects.filter(user=request.user).values('song')
        playlists = Playlist.objects.filter(owner=request.user)
        recently_played = RecentlyPlayed.objects.filter(user=request.user)
        return render(request, 'user_profile.html', {'liked_songs': liked_songs, 'playlists': playlists, 'recently_played': recently_played})
    else:
        return redirect('login')