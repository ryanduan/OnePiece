# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'awang'

from test.test_basic import TestBasic, build_data
from models.caricature import Caricature
from models.animation import Animation
from models.music import Music


class TestMusicModel(TestBasic):

    def setUp(self):
        super().setUp()

    def test_car(self):
        data = build_data(op='car')
        car = Caricature(**data)
        self.session.add(car)
        self.session.commit()
        self.assertEqual(car.part_id, data.get('part_id'))
        self.assertEqual(car.image_id, data.get('image_id'))
        self.assertEqual(car.name, data.get('name'))
        self.assertEqual(car.artist, data.get('artist'))

    def test_ani(self):
        data = build_data(op='ani')
        ani = Animation(**data)
        self.session.add(ani)
        self.session.commit()
        self.assertEqual(ani.video_uri, data.get('video_uri'))
        self.assertEqual(ani.name, data.get('name'))
        self.assertEqual(ani.artist, data.get('artist'))
        self.assertEqual(ani.lang, data.get('lang'))

    def test_musi(self):
        data = build_data()
        music = Music(**data)
        self.session.add(music)
        self.session.commit()
        self.assertEqual(music.mid, data.get('mid'))
        self.assertEqual(music.music_uri, data.get('music_uri'))
