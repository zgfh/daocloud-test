#!/usr/bin/env python
# -*- coding: utf-8 -*-



"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io
@time: 16/4/7 下午7:40
"""


import os,time,datetime
import logging
LOG=logging.getLogger(__name__)


from flask import Flask,request
from flask_restful import Resource, Api



from raven.contrib.flask import Sentry

sentry = Sentry(dsn=os.getenv('APP_SENTRY_KEY',''))

app = Flask(__name__)
sentry.init_app(app)
api = Api(app)

class home(Resource):
    def get(self):
        return {'app': 'daocloud-test'}
    def post(self):
        return self.get(self)



class time(Resource):
    def get(self):
        return str(datetime.datetime.now())

    def post(self):
        return self.get(self)

api.add_resource(home, '/')

api.add_resource(time, '/time')


def run():
    app.run(host='0.0.0.0',debug=True)

if __name__ == '__main__':
    run()