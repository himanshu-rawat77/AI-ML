

pip install spotipy

"""# Importing Libraries"""

import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt

"""# API SECTION"""

#API Keys
client_id = '421ac00cea374e5b8bfb78470f863389'
client_secret = '61481425949349d597eb83e3192fbfca'

#Get Access Token
client_crendential_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_crendential_manager)

"""# Plotting of Data"""

#Get data
playlist_id = '37i9dQZF1DWZNJXX2UeBij'
results=sp.user_playlist_tracks(user= '31kmzguuntrxcg2yw2h6qvrjxnqa', playlist_id=playlist_id)
tracks=results['items']
#Extract Information
track_names= []
album_names= []
artist_names = []

for track in tracks:
    track_names.append(track['track']['name'])
    album_names.append(track['track']['album']['name'])
    artist_names.append(track['track']['artists'][0]['name'])


# Creating a DataFrame
data = {'Tracks' : track_names,
        'Albums': album_names,
        'Artists': artist_names}
df = pd.DataFrame(data)
# Plotting the number of tracks per album
df['Albums'].value_counts().plot(kind='bar')
plt.xlabel('Albums')
plt.ylabel('No. of Tracks')
plt.title("No. of Tracks per Album")
plt.show()

# Plotting the top 10 tracks of artists
df['Artists'].value_counts().head(10).plot(kind='bar')
plt.xlabel('Artists')
plt.ylabel('No. of Tracks')
plt.title('Top 10 Tracks of Artists')
plt.show()