from django.db import models
from django.conf import settings

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    artist = models.CharField(max_length=100, null=False)
    song = models.FileField(upload_to='songs/tracks/', null=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    album = models.ImageField(upload_to='songs/album/', null=True)

    def __str__(self):
        return "{}-{}-{}-{}-{}-{}".format(self.id, self.title, self.artist, self.song, self.uploader, self.album)