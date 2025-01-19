import os

from flask import Flask, session

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)

client_id = "6eb97510d91b4fb7b05aadc57fc8af48"
client_secret = "32484a0911b94b0db3a35b2b1e8a788e"
redirect_uri = "http://localhost:3000"
scope = "playlist-read-private"



if __name__ == '__main__':
    app.run(debug=True)


