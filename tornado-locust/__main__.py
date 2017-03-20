"""Simple tornado demonstration app
"""

import tornado
import tornado.web

from .api_handler import ApiHandler

from .config import TORNADO_PORT

def main():
    """start the tornado server application
    """

    application_tornado = tornado.web.Application(
        [
            (r"/api", ApiHandler,),
        ],
    )
    application_tornado.listen(TORNADO_PORT, decompress_request=True)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
