import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import psycopg2

# Authentication credentials
client_id = '**********'
client_secret = '***********'

# Spotify API Configuration
sy = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
))

db_config = {
    'host': '*******',
    'dbname': '*******',
    'port': '******',
    'user': '*******',
    'password': '*********'
}

# Database Init
connection = psycopg2.connect(**db_config)
cursor = connection.cursor()

# Values filter
categories = ["Prog rock","Grunge", "jazz", "rock"]
limit = 50

# Extract all artists list from Spotify with genre match
def extract_artists():
    result = []
    for category in categories:
        artists = sy.search(q=f'genres:"{category}', type='artist', limit=limit)

    # Loop each artist and get the values
        for artist in artists['artists']['items']:
            id = artist['id']
            name = artist['name']
            genres = artist['genres']
            followers = artist['followers']['total'] #int
            popularity = artist['popularity'] #int

            if not genres:
                genres = None
            else:
                genres = ', '.join(genres)

            result.append((id, name, genres, followers, popularity))
        
        return result

# Transform those values and stored. 
def load_artist_values(data):    
    # Initialize insert_query outside the loop
    insert_query = """
        INSERT INTO artists (id, name, genres, followers, popularity) 
        VALUES (%s, %s, %s, %s, %s)
    """
    for artist in data:
        artist_id = artist[0]
        name = artist[1]
        genres = artist[2]
        followers = artist[3]
        popularity = artist[4]

        if genres is not None:
            # Convert genres list to a string array
            genres_array = "{" + ", ".join(f"'{genre}'" for genre in genres) + "}"
        else:
            genres_array = None  # Set genres_array to None if genres is None

        try:
            # Check if the artist already exists in the database
            cursor.execute("SELECT id FROM artists WHERE id = %s", (artist_id,))
            existing_artist = cursor.fetchone()

            if existing_artist:
                # If the artist already exists, delete the existing record
                delete_query = "DELETE FROM artists WHERE id = %s"
                cursor.execute(delete_query, (artist_id,))

            # Insert a new artist record
            insert_query = """
                INSERT INTO artists (id, name, genres, followers, popularity) 
                VALUES (%s, %s, %s, %s, %s)
                """
            cursor.execute(insert_query, (artist_id, name, genres_array, followers, popularity))
        except psycopg2.IntegrityError as e:
            connection.rollback()  # Rollback the transaction
            print(f"Error: {e}. Attempting to remove duplicate record with ID: {artist_id}")
            # Log or handle the error as needed
        
    connection.commit()

try:
    artists = extract_artists()
    load_artist_values(artists)
    print("Data loaded successfully!")
except Exception as e:
    print("Error:", str(e))
finally:
    cursor.close()
    connection.close()
