import os
import pickle

from models import Artist

if __name__ == "__main__":
    ## Read the file
    root_directory = os.getcwd()  # Get the current working directory
    data_folder = "spotify/data/artists"
    path = os.path.join(root_directory, data_folder, "artists.pickle")
    print("Start reading file")
    with open(path, 'rb') as file:
        data = pickle.load(file)
    print("Finish reading file")

    # Convert a dataframe into a list of dictionaries
    data = data.to_dict(orient='records')

    print("Start saving data to the 'Artist' table")
    # Insert each row into the Artist table
    for row in data:
        Artist.objects.create(
            artist=row['artist'],
            uri=row['uri'],
            genres=row['genres'],
            num_of_followers=row['num_of_followers'],
            popularity=row['popularity'],
        )
    print("Finish saving data to the 'Artist' table")