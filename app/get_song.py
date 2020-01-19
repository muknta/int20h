import requests
import json
from api_tokens import token


def get_url_song_by_lyrics(lyric):
    data = {
        'url': lyric,
        'return': 'timecode,apple_music,deezer,spotify',
        'api_token': token
    }

    result = requests.post('https://api.audd.io/', data=data)
    dict_result = json.loads(result.text)
    return dict_result['result']['deezer']['link']


def get_url_song_by_voice(voice):
    data = {
        'url': voice,
        'method': 'recognizeWithOffset',
        'api_token': token
    }

    result = requests.post('https://api.audd.io/', data=data)
    dict_result = json.loads(result.text)
    return dict_result


def get_url_song_by_text(text):
    data = {
        'q': text,
        'method': 'findLyrics',
        'api_token': token
    }

    result = requests.post('https://api.audd.io/', data=data)
    dict_result = json.loads(result.text)
    return dict_result['result'][0]['full_title']


if __name__ == "__main__":
    # print(get_url_song_by_lyrics('https://audd.tech/example1.mp3'))
    # print(get_url_song_by_voice('https://audd.tech/example_h1.ogg'))
    print(get_url_song_by_text("adele hello"))
