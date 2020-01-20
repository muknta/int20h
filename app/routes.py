from app import app
from flask import render_template, jsonify, request
from config import API
from .route_handlers import *


@app.route('/')
@app.route('/int20h')
def init():
    return render_template('init_page.html')


@app.route(f'{API}/song/recognize', methods=['POST'])
def recognize_song():
    data = request.get_json()
    recognition_type = data.get('type')
    if recognition_type is not None:
        if recognition_type == 'text':
            return recognize_song_by_text(data)
        elif recognition_type == 'voice':
            return recognize_song_by_voice(data)
        elif recognition_type == 'sound':
            return recognize_song_by_sound(data)
    return jsonify(msg='Invalid data', result=False), 400
