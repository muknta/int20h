from gevent import monkey
monkey.patch_all()
from app import app

app.debug = True


def main():
    # app.run('0.0.0.0', 5000)
    # # http = WSGIServer(('127.0.0.1', 5000), app)
    # # http.serve_forever()
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
