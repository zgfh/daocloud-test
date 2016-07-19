#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io
@time: 16/7/19 下午7:19
"""

from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    #print "headers:%s "% request.headers
    if 'X-Forwarded-For' in  request.headers:
        print "X-Forwarded-For: %s"% request.headers['X-Forwarded-For']
    else:
        print "X-Forwarded-For: "
    if 'X-Real-IP' in  request.headers:
        print "X-Real-IP: %s"% request.headers['X-Real-IP']
    else:
        print "X-Real-IP: "

    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

