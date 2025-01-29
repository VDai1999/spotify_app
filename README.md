# Spotify Simulation App

This is a Django-based web application that simulates core functionalities of Spotify, allowing users to browse songs, create playlists, and stream music. The project demonstrates the integration of backend logic with a responsive frontend, handling user authentication, playlist management, and song playback.

## Features

- **User Authentication**: Sign up, log in, and manage user accounts.
- **Song Library**: Browse through a collection of songs, artists, and albums.
- **Playlists**: Users can create, edit, and delete their playlists.
- **Song Playback**: Users can play, pause, and skip tracks within playlists.
- **Search**: Users can search for songs, artists, and albums.

## Installation

### Prerequisites

- Python 3.8 or higher
- Django 4.0 or higher
- PostgreSQL (or any database of your choice)

### Setup Instructions

1. **Clone the repository:**

   ```bash
   git https://github.com/VDai1999/spotify_app.git
   cd spotify_app
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   Update `settings.py` with your database configuration. Example for PostgreSQL:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'spotify_db',
           'USER': 'your_db_user',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

   Then, run migrations:

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The application should now be running at `http://127.0.0.1:8000/`.

## Usage

- **Home Page**: The landing page displays featured playlists and recently added songs.
- **User Authentication**: You can sign up or log in from the navigation bar.
- **Library**: Browse all available songs, artists, and albums.
- **Playlist Creation**: Once logged in, you can create your own playlists and add songs.
- **Playback**: Play songs directly from the playlist page with basic controls (play, pause, skip).
- **Search**: Use the search bar to look for specific songs, albums, or artists.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: PostgreSQL (or another Django-compatible database)
- **Authentication**: Django's built-in authentication system

## References

1. Artist dataset: [Spotify Artist Metadata Top 10k](https://www.kaggle.com/datasets/jackharding/spotify-artist-metadata-top-10k)
