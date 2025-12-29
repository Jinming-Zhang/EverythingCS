import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

clientId = "2ca75c9889644cc39c918a15d81c416f"
clientSecret = "7a4b2a9ca14d488a8bbc9b9c2e779163"


class sptipy_wrapper:
    def __init__(self, id, secret) -> None:
        self.clientId = id
        self.clientSecret = secret
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
            client_id=clientId, client_secret=clientSecret))

    def retrieve_spotify_features(self, song_name, artist_name):
        result = self.sp.search(q=song_name, limit=20)
        id = ''
        popularity = 0
        # find id of the song
        for info in result['tracks']['items']:
            if info == None:
                return None
            artists = info['artists']
            for artist in artists:
                a_name = artist['name']
                if a_name in artist_name:
                    id = info['id']
                    popularity = info['popularity']
                    break
        # retreive features of the song
        features = self.sp.audio_features(id)[0]
        if(features != None):
            features['popularity'] = popularity
        return features


class song_info:
    def __init__(self, name, artist) -> None:
        self.name = name
        self.artist = artist

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, song_info) and __o.name == self.name and __o.artist == self.artist

    def __hash__(self) -> int:
        return hash(self.name+self.artist)


file_path = 'D:\\Projects\\ObsidianNotes\\NEU_Courses_Repo\\FundamentalsAI\\Assignments\\PythonUtils\\finalSpotify\\datasets\\charts.csv'

df = pd.read_csv(file_path)
spwrapper = sptipy_wrapper(clientId, clientSecret)
target_features = ['danceability',
                   'energy', 'speechiness', 'instrumentalness', 'tempo']
result = {}
unsearchable = []
for song_data in df.iterrows():
    song = song_data[1]
    song_name = song['song']
    artist = song['artist']
    rank = song['peak-rank']
    song_d = song_info(song_name, artist)
    if song_d in result and result[song_d]['rank'] > rank:
        result[song_d]['rank'] = rank
    else:
        features = {}
        features['rank'] = rank
        song_features = spwrapper.retrieve_spotify_features(song_name, artist)
        if (song_features is None):
            unsearchable.append(song_name)
            continue
        for f in target_features:
            features[f] = song_features[f]
        result[song_d] = features
c = result
