from gevent import monkey
import os
monkey.patch_all()
from app import app

app.debug = True

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
