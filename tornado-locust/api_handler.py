"""Simple API handler for demo
"""

import tornado
from tornado.web import gen

class ApiHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self):
        self.write("OK");
