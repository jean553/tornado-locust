"""Simple API handler for demo
"""

import tornado

class ApiHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello");
