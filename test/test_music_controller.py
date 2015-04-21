# -*- coding: utf-8 -*-

"""
Description
"""
import time

__author__ = 'awang'


import json
from unittest.mock import patch
from urllib.parse import urlencode
from tornado.test.web_test import wsgi_safe
from test.test_basic import TestControllerBasic, build_data, byte_decode
from controllers.read_controller import ReadCaricature, WatchAnimation, ListenMusic
from controllers.write_controller import CreateAnimation, CreateCaricature, CreateMusic
from models.caricature import Caricature
from models.animation import Animation
from models.music import Music
from sqlalchemy.orm import Session, Query
from sqlalchemy.exc import SQLAlchemyError


@wsgi_safe
class TestCreateMusic(TestControllerBasic):
    """"""
    Handler = CreateMusic

    def setUp(self):
        super().setUp()
        self.data = build_data()

    def test_post(self):
        response = self.fetch('/', method='POST',
                              body=urlencode(dict(data=json.dumps(self.data))))
        res = json.loads(response.body.decode('utf-8'))
        self.assertEqual(res.get('error_code'), 20000)
        # 看看是不是真的写入了数据库
        music = self.session.query(Music).filter_by(
            media_id=self.data.get('music_uri'), owner_id=self.data.get('music_uri')
        ).first()
        self.assertIsNotNone(music)
        self.assertEqual(music.artist, self.data.get('artist'))

    def test_exc(self):
        """"""
        # SQLAlchemyError
        data = build_data()
        with patch.object(Session, 'commit', side_effect=SQLAlchemyError):
            response = self.fetch('/', method='POST',
                                  body=urlencode(dict(data=json.dumps(data))))
            res = json.loads(response.body.decode('utf-8'))
            self.assertEqual(res.get('error_code'), 20101)


