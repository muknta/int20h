import requests
from config import API_REC_TOKEN
from flask import jsonify


def recognize_song_by_text_handler(text):
    if text is not None:
        data = {
                'q': text,
                'api_token': API_REC_TOKEN
        }
        return requests.post("https://api.audd.io/findLyrics/", data=data).json(), 200
    else:
        return jsonify(msg='Invalid data', result=False), 200


def recognize_song_by_voice_handler(voice):
    if voice is not None:
        data = {
            'url': voice,
            'api_token': API_REC_TOKEN
        }
        return requests.post("https://api.audd.io/recognizeWithOffset/", data=data).json(), 200
    else:
        return jsonify(msg='Invalid data', result=False), 200


def recognize_song_by_sound_handler(url):
    if url is not None:
        data = {
                'url': url,  # Todo: url = heroku..../song/download&filename
                'return': 'timecode,apple_music,deezer,spotify',
                'api_token': API_REC_TOKEN
        }
        return requests.post('https://api.audd.io/', data=data).json(), 200
    else:
        return jsonify(msg='Invalid data', result=False), 200
