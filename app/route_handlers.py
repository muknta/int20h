import requests
from config import API_REC_TOKEN
from flask import jsonify


def recognize_song_by_text(request):
    text = request.get('data')
    if text is not None:
        data = {
                'q': text,
                'api_token': API_REC_TOKEN
        }
        return requests.post("https://api.audd.io/findLyrics/", data=data).json(), 200
    else:
        return jsonify(msg='Invalid data', result=False), 400


def recognize_song_by_voice(request):
    voice = request.get('data')
    if voice is not None:
        data = {
            'url': voice,
            'api_token': API_REC_TOKEN
        }
        return requests.post("https://api.audd.io/recognizeWithOffset/", data=data).json(), 200
    else:
        return jsonify(msg='Invalid data', result=False), 400


def recognize_song_by_sound(request):
    lyrics = request.get('data')
    if lyrics is not None:
        data = {
                'url': lyrics,
                'return': 'timecode,apple_music,deezer,spotify',
                'api_token': API_REC_TOKEN
        }
        return requests.post('https://api.audd.io/', data=data).json(), 200
    else:
        return jsonify(msg='Invalid data', result=False), 400
