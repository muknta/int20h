from app.get_path import get_path
from app import app


API = '/api/v1'
API_REC_TOKEN = '632a3e608f3f7804462b1055927f0e9a'
app.config['ALLOWED_EXTENSIONS'] = ['MP3', 'OGG']
app.config['UPLOAD_FOLDER'] = get_path()