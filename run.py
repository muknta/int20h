from gevent.pywsgi import WSGIServer
from app import app
from gevent import monkey; monkey.patch_all()

app.debug = True


def main():
    monkey.patch_all()
    http = WSGIServer(('127.0.0.1', 5000), app)
    http.serve_forever()


if __name__ == '__main__':
    main()
