from django.urls import path
from music import views
# from django.conf.urls.static import static
from django.conf.urls.static import static
from MusicPlayer import settings

app_name = 'music'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('songs', views.SongListView.as_view(), name = 'song_list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

