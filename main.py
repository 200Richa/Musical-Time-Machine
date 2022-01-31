# Client Credentials Flow.
from secrets import CLIENT_SECRET_KEY, CLIENT_ID, BASE_ENDPOINT, USER_ID
import requests
from bs4 import BeautifulSoup

# Scraping Billboard
date = '2000-08-12'
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
website = response.text
# Making Soup
soup = BeautifulSoup(website, "html.parser")
songs = list()
for song in soup.select("li.o-chart-results-list__item h3#title-of-a-story"):
    songs.append(song.getText().strip('\n'))



# Spotify Authorization
payload = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'grant_type': 'client_credentials',
    }
TOKEN_URL = 'https://accounts.spotify.com/api/token'
res = requests.post(TOKEN_URL, auth=(CLIENT_ID, CLIENT_SECRET_KEY), data=payload)
res.raise_for_status()
res_data = res.json()
access_token = res_data.get('access_token')

data = {
    "name": "New Playlist",
    "description": "New playlist description",
}
headers = {
    "Content-Type": "application/json; charset=utf-8",
    'Authorization': f"Bearer {access_token}"
}
response = requests.post(f"{BASE_ENDPOINT}/users/{USER_ID}/playlists", headers=headers,json=data)
response.raise_for_status()
print(response.json())


