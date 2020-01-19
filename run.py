from gevent.pywsgi import WSGIServer
from app import app
from gevent import monkey; monkey.patch_all()

monkey.patch_all()
app.debug = True


"Start gevent WSGI server"
# use gevent WSGI server instead of the Flask
http = WSGIServer(('127.0.0.1', 5000), app)
# TODO gracefully handle shutdown
http.serve_forever()

