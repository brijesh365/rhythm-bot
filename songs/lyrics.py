import requests

import settings

BASE_URL = 'https://api.musixmatch.com/ws/1.1/'
LYRICS_MATCHER = 'matcher.lyrics.get'
FORMAT_URL = '?format=json&callback=callback&q_track={query}&apikey={api_key}'
URL = BASE_URL + LYRICS_MATCHER + FORMAT_URL


def search(query):
    try:
        response = requests.get(URL.format(query=query, api_key=settings.MUSIXMATCH_KEY))
        return response.json()['message']['body']['lyrics']['lyrics_body']
    except Exception as e:
        print(e)
