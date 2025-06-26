import os
from pprint import pp
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = "http://127.0.0.1:1234"
SCOPE = "user-library-read"

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

results = spotify.current_user_playlists()["items"]
playlist_names = [playlist["name"] for playlist in results]

print("Playlists:" + "\n" + "--------------------")
for index, name in enumerate(playlist_names):
    print(f"{index + 1}. {name}")
print()

while True:
    try:
        playlist_index = int(input("Choose a number: "))
    except ValueError:
        continue
    print()
    if playlist_index > 0 and playlist_index <= len(playlist_names):
        playlist_index -= 1
        break

songs = spotify.playlist_items(results[playlist_index]["id"], limit=20)["items"]
tracks = [song["track"] for song in songs]
track_names_and_artists = [(track["name"], track["artists"][0]["name"]) for track in tracks]

print("Songs:"+ "\n" + "--------------------")
for name, artist in track_names_and_artists:
    print(f"{name} - {artist}")
