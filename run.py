from gevent import monkey
monkey.patch_all()
from app import app
import os

app.debug = True


def main():
    # app.run('0.0.0.0', 5000)
    # # http = WSGIServer(('127.0.0.1', 5000), app)
    # # http.serve_forever()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
