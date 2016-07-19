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
    real_ip=''
    forward_ip=''
    if 'X-Forwarded-For' in  request.headers:
        forward_ip=request.headers['X-Forwarded-For']
    print "X-Forwarded-For: %s".format(forward_ip)
    if 'X-Real-IP' in  request.headers:
        real_ip=request.headers['X-Real-IP']
    print "X-Real-IP: %s".format(real_ip)

    return str({'real_ip':real_ip,'forward_ip':forward_ip})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

