import os
import pickle
import pandas as pd
from models import Song

if __name__ == "__main__":
    ## Read the file
    root_directory = os.getcwd()  # Get the current working directory
    data_folder = "spotify/data/processed_global_top_songs"
    path = os.path.join(root_directory, data_folder, "full_data.pickle")
    print("Start reading file")
    with open(path, 'rb') as file:
        data = pickle.load(file)
    print("Finish reading file")


    # Convert the frame into a list of dictionaries
#     # Convert a dataframe into a list of dictionaries
#     data = data.to_dict(orient='records')

#     print("Start saving data to the 'Song' table")
#     # Insert each row into the Song table
#     for row in data:
#         Song.objects.create(
#             uri=row['uri'],
#             artist_names=row['artist_names'],
#             track_name=row['track_name'],
#             acousticness=row['acousticness'],
#             danceability=row['danceability'],
#             duration_ms=row['duration_ms'],
#             energy=row['energy'],
#             instrumentalness=row['instrumentalness'],
#             liveness=row['liveness'],
#             loudness=row['liveness'],
#             mode=row['mode'],
#             speechiness=row['speechiness'],
#             tempo=row['tempo'],
#             time_signature=row['time_signature'],
#             valence=row['valence'],
#             uri_artist=row['uri_artist'],
#             artist_pop=row['artist_pop'],
#             num_followers=row['num_followers'],
#             artist_genres=row['artist_genres'],
#             track_pop=row['track_pop'],
#         )
#     print("Finish saving data to the 'Song' table")


# # data = pd.DataFrame(columns=["uri", "artist_names", "track_name", 
# #                                   "acousticness", "danceability", "duration_ms",
# #                                   "energy", "instrumentalness", "liveness", 
# #                                   "loudness", "mode", "speechiness", "tempo", 
# #                                   "time_signature", "valence", "uri_artist", 
# #                                   "artist_pop", "num_followers", 
# #                                   "artist_genres", "track_pop"])