#! /usr/bin/python
# -*- coding:utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import datetime

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        response = str(datetime.datetime.utcnow())
        self.write(response)

if __name__ == "__main__":
    app = tornado.web.Application(handlers=[(r"/time", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(5000)
    tornado.ioloop.IOLoop.instance().start()