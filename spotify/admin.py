from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "user_name", "display_name", "first_name", "last_name", "email", "password", "phone_number", "date_of_birth", "gender", "status", "email_verified", "subscription_type", "country", "created_at", "updated_at"]


class PlaylistAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "description", "created_at", "updated_at"]


class SongAdmin(admin.ModelAdmin):
    list_display = ["uri" , "artist_names", "track_name", "acousticness", "danceability", "duration_ms",
                    "energy", "instrumentalness", "liveness", "loudness", "mode", "speechiness", "tempo",
                    "time_signature", "valence", "uri_artist", "artist_pop", "num_followers", "artist_genres",
                    "track_pop"]
    search_fields = ['track_name', 'artist_names']
    list_filter = ['artist_names']


class PlaylistSongAdmin(admin.ModelAdmin):
    list_display = ["playlist", "song", "added_at"]


class ArtistAdmin(admin.ModelAdmin):
    list_display = ["artist", "uri", "genres", "num_of_followers", "popularity"]


class FavoriteSongAdmin(admin.ModelAdmin):
    list_display = ["user", "song", "added_at"]


admin.site.register(User, UserAdmin)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(PlaylistSong, PlaylistSongAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(FavoriteSong, FavoriteSongAdmin)