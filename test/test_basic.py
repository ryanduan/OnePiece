# -*- coding: utf-8 -*-

"""
Description
"""
import time

__author__ = 'awang'


from models.dao import Dao
from models.op_cache import OPCache
import unittest
from tornado.test.web_test import SimpleHandlerTestCase
import random
from models.caricature import Caricature
from models.animation import Animation
from models.music import Music


class TestBasic(unittest.TestCase):
    """测试的基类"""

    def setUp(self):
        """初始化数据库表结构， 完成数据库session，缓存及redis连接"""
        Dao.init_db_uri()
        self.session = Dao.session()
        Dao.init_table_schema()
        self.cache = OPCache()
        self.rds = Dao.redis()
        self.session.rollback()

    def tearDown(self):
        """清除表里的数据，redis里的数据"""
        self.session.rollback()
        self.session.flush()
        self.session.query(Music).delete()
        self.session.query(Caricature).delete()
        self.session.query(Animation).delete()
        self.rds.flushdb()


class TestControllerBasic(SimpleHandlerTestCase, TestBasic):
    """controller的测试基类"""

    def setUp(self):
        """这里初始化需要的数据，但是好像每个controller不一样，数据也就不太一样了"""
        super().setUp()


def build_data(op=None):
    """生成测试数据，这里生成一个可以写入到music_basic的dict"""
    if op == 'car':
        return dict(
            part_id=random.randint(1, 800),
            image_uri='/image/{}.mp4'.format(random.randint(1, 2000)),
            name='name {}'.format(random.randint(1, 2000)),
            image_id=random.randint(1, 2000),
            artist='artist{}'.format(random.randint(1, 300)),
        )
    elif op == 'ani':
        return dict(
            video_uri='/video/{}.mp4'.format(random.randint(1, 800)),
            name='name {}'.format(random.randint(1, 2000)),
            lang=random.randint(1, 3),
            artist='artist{}'.format(random.randint(1, 300)),
            create_time=int(time.time()),
        )
    else:
        return dict(
            name='name {}'.format(random.randint(1, 2000)),
            create_time=int(time.time()),
            artist='artist{}'.format(random.randint(1, 300)),
            music_uri='/music/{}.mp3'.format(random.randint(1, 300)),
            lyrics='test lyrics',
            lyricist='lyricist',
            composer='composer',
        )


def byte_decode(res):
    """# TODO 在windows下会是bytes，需要处理一下"""
    return bytes.decode(res)


def exc_data():
    """这里返回一组有异常的数据进行针对性测试"""
    return []
