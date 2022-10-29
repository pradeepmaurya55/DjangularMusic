from django.urls import path
from .views import AllSongsListView,SongView,PostSongsView
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('songs/' , AllSongsListView.as_view(), name="songs-all"),
    path('songs/<int:id>', SongView.as_view(),name="song"),
    path('songs1/', csrf_exempt(PostSongsView.as_view()),name="postSong")
]