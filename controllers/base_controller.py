# -*- coding: utf-8 -*-

"""
Description
"""
from tornado.web import RequestHandler
from models.dao import Dao
from models.util import cached_property
from models.op_cache import OPCache
import json
import logging

__author__ = 'awang'


class BaseController(RequestHandler):
    """"""

    @cached_property
    def op_session(self):
        """"""
        return Dao.session()

    @cached_property
    def data(self):
        data = self.get_argument('data', None)
        if data is not None:
            return json.loads(data)
        return dict()

    def pack_img(self, img):
        """:return dict
        把一个Caricature对象封装成dict，用来缓存"""
        return dict(
            part_id=img.part_id,
            image_id=img.image_id,
            image_uri=img.image_uri,
            artist=img.artist,
        )

    def pake_music(self):
        """"""
        return dict()

    def pake_ani(self):
        """"""
        return dict()

    def pack_music(self, music):
        return music

    @cached_property
    def cache(self):
        """"""
        return OPCache()

    def do_write(self, code, msg='', **data):
        """"""
        if code != 20000:
            logging.warning(msg)
        else:
            logging.info(msg)
        self.write(json.dumps(dict(error_code=code, data=data, msg=msg)))
