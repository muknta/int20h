from app import app
from flask import render_template, request, send_from_directory
from config import API
from .route_handlers import *

import os
from flask import flash, redirect, url_for
from werkzeug.utils import secure_filename


def allowed_file(filename):
    if not "." in filename:
        return False
    
    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_EXTENSIONS"]:
        return True
    else:
        return False


# Todo: move functionality to recognize_song_by_sound(recognize_song_by_voice), Remove method.
@app.route('/upload-song', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if request.files["track"]:
            track = request.files["track"]
            print(track)

            if track.filename == "":
                print("Image must have a filename")
                return redirect(request.url)
            
            if not allowed_file(track.filename):
                print("That file extension is not allowed")
                return redirect(request.url)

            else:
                filename = secure_filename(track.filename)

                track.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

            # TODO : make request to API then delete a file

            # os.remove(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            print("File saved")

            return redirect(request.url)

    return render_template("init_page.html")


@app.route('/song/download')
def download_song():
    # Doesn't need a check of existing.
    return send_from_directory(directory=app.config['UPLOAD_FOLDER'], filename=request.args.get('song'))


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
