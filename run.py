from gevent import monkey

monkey.patch_all()
from app import app

app.debug = True

if __name__ == '__main__':
    app.run()
