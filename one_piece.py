# -*- coding: utf-8 -*-

"""
Description
"""

import os.path
import sys
sys.path.insert(0, './models/')
sys.path.insert(0, './tornado/')

import tornado.options
from tornado.options import options
import tornado.web
from tornado.httpserver import HTTPServer
import tornado.ioloop
from models.dao import Dao
import logging

from controllers.read_controller import ReadCaricature, WatchAnimation, ListenMusic
from controllers.write_controller import CreateAnimation, CreateCaricature, CreateMusic

__author__ = 'awang'


class Application(tornado.web.Application):
    """"""

    def __init__(self):
        """"""
        urls = [
            (ReadCaricature.url, ReadCaricature),
            (WatchAnimation.url, WatchAnimation),
            (ListenMusic.url, ListenMusic),
            (CreateMusic.url, CreateMusic),
            (CreateCaricature.url, CreateCaricature),
            (CreateAnimation.url, CreateAnimation),
        ]
        settings = dict(
            xsrf_cookies=False
        )
        tornado.web.Application.__init__(self, urls, **settings)

if __name__ == '__main__':
    """"""
    options.define(name='config', default='dev')
    options.define(name='port', default=21002)
    options.define(name='process', default=1)

    tornado.options.parse_command_line()

    Dao.init_db_uri(options.config)
    if options.config == 'unittest':
        Dao.init_table_schema()

    app = Application()
    server = HTTPServer(app, xheaders=True)
    server.bind(int(options.port))
    server.start(num_processes=int(options.process))

    tornado.ioloop.IOLoop.instance().start()