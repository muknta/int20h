from gevent import monkey
import os
monkey.patch_all()
from app import as application

application.debug = True


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    application.run(host='0.0.0.0', port=port)
