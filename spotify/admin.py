from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "user_name", "display_name", "first_name", "last_name", "email", "password", "phone_number", "date_of_birth", "gender", "status", "email_verified", "subscription_type", "country", "created_at", "updated_at"]


class PlaylistAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "description", "created_at", "updated_at"]


class SongAdmin(admin.ModelAdmin):
    list_display = ('track_name', 'artist_names', 'duration_ms', 'uri', 'track_pop', 'artist_pop')
    search_fields = ('track_name', 'artist_names')
    list_filter = ('artist_genres',)


class PlaylistSongAdmin(admin.ModelAdmin):
    list_display = ["playlist", "song", "added_at"]



admin.site.register(User, UserAdmin)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(PlaylistSong, PlaylistSongAdmin)