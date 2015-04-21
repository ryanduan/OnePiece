# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'awang'

from test.test_basic import TestBasic, build_data, byte_decode
import json

# TODO mock RedisError


class TestMusicCache(TestBasic):
    """"""

    def setUp(self):
        super().setUp()

    def test_cache_music(self):
        """"""
        music = build_data()
        music['mid'] = 1
        self.cache.cache_music(music)
        res = self.rds.get(self.cache.music_key.format(music.get('mid')))
        res = byte_decode(res)
        test_music = json.loads(res)
        self.assertEqual(test_music, music)

    def test_get_music(self):
        music = build_data()
        music['mid'] = 1
        self.rds.set(self.cache.music_key.format(music.get('mid')), music)
        test_music = self.cache.get_music(music.get('mid'))
        self.assertEqual(music, test_music)

    def test_cache_multi_music(self):
        m1 = build_data()
        m1['mid'] = 1
        m2 = build_data()
        m2['mid'] = 2
        m3 = build_data()
        m3['mid'] = 3
        m4 = build_data()
        m4['mid'] = 4
        music_list = [m1, m2, m3, m4]
        self.cache.cache_multi_music(music_list)
        for m in music_list:
            res = self.rds.get(self.cache.music_key.format(m.get('mid')))
            res = byte_decode(res)
            tm = json.loads(res)
            self.assertEqual(m, tm)

    def test_get_multi_music(self):
        m1 = build_data()
        m1['mid'] = 1
        m2 = build_data()
        m2['mid'] = 2
        m3 = build_data()
        m3['mid'] = 3
        m4 = build_data()
        m4['mid'] = 4
        music_list = [m1, m2, m3, m4]
        data = dict(
            [(self.cache.music_key.format(m.get('mid')),
              json.dumps(m)) for m in music_list])
        self.rds.mset(**data)
        res = self.cache.get_multi_music([1, 2, 3, 4])
        for m in music_list:
            self.assertEqual(m, res.get(m.get('mid')))

    def test_clear_music(self):
        m1 = build_data()
        m1['mid'] = 1
        m2 = build_data()
        m2['mid'] = 2
        m3 = build_data()
        m3['mid'] = 3
        m4 = build_data()
        m4['mid'] = 4
        music_list = [m1, m2, m3, m4]
        data = dict(
            [(self.cache.music_key.format(m.get('mid')),
              json.dumps(m)) for m in music_list])
        self.rds.mset(**data)
        self.cache.clear_music(mid=m1.get('mid'))
        self.cache.clear_music(mid_list=[m.get('mid') for m in music_list])
        for m in music_list:
            self.assertIsNone(self.rds.get(self.cache.music_key.format(m.get('mid'))))
