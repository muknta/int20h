from gevent import monkey
from gevent.pywsgi import WSGIServer

monkey.patch_all()
from app import app
import os

app.debug = True


def main():
    # app.run('0.0.0.0', 5000)
    port = int(os.environ.get('PORT', 5000))
    http = WSGIServer(('0.0.0.0', port), app)
    http.serve_forever()


if __name__ == '__main__':
    main()
