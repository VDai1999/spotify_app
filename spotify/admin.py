from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "user_name", "display_name", "first_name", "last_name", "email", "password", "phone_number", "date_of_birth", "gender", "status", "email_verified", "subscription_type", "country", "created_at", "updated_at"]

admin.site.register(User, UserAdmin)

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "description", "created_at", "updated_at"]

admin.site.register(Playlist, PlaylistAdmin)


class SongAdmin(admin.ModelAdmin):
    list_display = ["title", "artist", "album", "duration", "release_date", "genre"]

admin.site.register(Song, SongAdmin)

class PlaylistSongAdmin(admin.ModelAdmin):
    list_display = ["playlist", "song", "added_at"]

admin.site.register(PlaylistSong, PlaylistSongAdmin)