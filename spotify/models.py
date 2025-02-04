from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone

import pycountry
from .utils import generate_random_username

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=150, unique=True, default=generate_random_username)
    display_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128) # Hashed password will be stored
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    # Gender
    GENDER_CHOICES = [
        ('female', 'Female'),
        ('male', 'Male'),
        ('other', 'Other'),
        ('prefer_not_to_say', 'Prefer not to say'),
        ('non_binary', 'Non-binary'),
    ]  
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='prefer_not_to_say')

    # Account status
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    # Email Verified
    email_verified = models.BooleanField(default=False)

    # Subscription/Plan
    SUBSCRIPTION_CHOICES = [
        ('free', 'Free'),
        ('invidual', 'Individual'),
        ('student', 'Student'),
        ('duo', 'Duo'),
        ('family', 'Family')
    ]
    subscription_type = models.CharField(max_length=20, choices=SUBSCRIPTION_CHOICES, default='free')

    # Country/Region
    COUNTRY_CHOICES = [(country.name, country.name) for country in pycountry.countries] + [('None', 'None')]
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, default='None')

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        # Check if password is already hashed
        if not self.password.startswith('pbkdf2_'):  # To avoid rehashing if already hashed
            self.password = make_password(self.password)

        # Ensure that user_name is unique
        while User.objects.filter(user_name=self.user_name).exists():
            self.user_name = generate_random_username()

        # Save changes
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user_name
    
class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Song(models.Model):
    uri = models.CharField(max_length=100, unique=True)
    artist_names = models.CharField(max_length=255)
    track_name = models.CharField(max_length=255)
    acousticness = models.FloatField()
    danceability = models.FloatField()
    duration_ms = models.IntegerField()
    energy = models.FloatField()
    instrumentalness = models.FloatField()
    liveness = models.FloatField()
    loudness = models.FloatField()
    mode = models.IntegerField(choices=[(0, 'Minor'), (1, 'Major')])
    speechiness = models.FloatField()
    tempo = models.FloatField()
    time_signature = models.IntegerField()
    valence = models.FloatField()
    uri_artist = models.CharField(max_length=100)
    artist_pop = models.IntegerField()
    num_followers = models.BigIntegerField()
    artist_genres = models.JSONField()
    track_pop = models.IntegerField()
    song_img_url = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.track_name} by {self.artist_names}"
    
class PlaylistSong(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name="playlist_songs")
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="song_playlists")
    added_at = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     unique_together = ("playlist", "song")  # Ensures a song can only appear once per playlist

    def __str__(self):
        return f"{self.song.title} in {self.playlist.name}"
    

class Artist(models.Model):
    artist = models.CharField(max_length=255)
    uri = models.CharField(max_length=100)
    genres = models.JSONField()
    num_of_followers = models.IntegerField()
    popularity = models.IntegerField()

    def __str__(self):
        return f"{self.artist}"