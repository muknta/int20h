from gevent import monkey
monkey.patch_all()

from gevent.pywsgi import WSGIServer
from app import app

app.debug = True


def main():
    http = WSGIServer(('127.0.0.1', 5000), app)
    http.serve_forever()


if __name__ == '__main__':
    main()
