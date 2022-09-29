import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="1ea410f7efe74892818c06e1c5efbeb4",
        client_secret="49db312a18824eadba214622c9dab69d",
        show_dialog=True,
        cache_path="token.txt"
    )
)




day = input("Please select date YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{day}"

response = requests.get(URL)
site = response.text


soup = BeautifulSoup(site, "html.parser")
for song in soup.select('li.o-chart-results-list__item h3.c-title'):
    print(f"{song.getText().strip()} - {sp.search( song.getText().strip())['tracks']['items'][0]['external_urls']['spotify']}")
