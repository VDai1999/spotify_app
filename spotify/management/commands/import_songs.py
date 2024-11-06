# import_csv.py
import csv
from django.core.management.base import BaseCommand
from spotify.models import Song

class Command(BaseCommand):
    help = 'Import songs from a CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to import')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            songs = []
            for row in reader:
                song = Song(
                    uri=row['uri'],
                    artist_names=row['artist_names'],
                    track_name=row['track_name'],
                    acousticness=row['acousticness'],
                    danceability=row['danceability'],
                    duration_ms=row['duration_ms'],
                    energy=row['energy'],
                    instrumentalness=row['instrumentalness'],
                    liveness=row['liveness'],
                    loudness=row['loudness'],
                    mode=row['mode'],
                    speechiness=row['speechiness'],
                    tempo=row['tempo'],
                    time_signature=row['time_signature'],
                    valence=row['valence'],
                    uri_artist=row['uri_artist'],
                    artist_pop=row['artist_pop'],
                    num_followers=row['num_followers'],
                    artist_genres=row['artist_genres'],
                    track_pop=row['track_pop']
                )
                songs.append(song)

            # Bulk create to save all objects at once
            Song.objects.bulk_create(songs)
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))
