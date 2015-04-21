# -*- coding: utf-8 -*-

"""
Description
"""
from models.op_error import OPError

__author__ = 'awang'

from models.dao import Dao
from redis import RedisError
import logging
import json


class OPCache(object):
    """歌曲缓存：
            缓存歌曲信息
    """
    rds = Dao.redis()

    music_key = 'music:{}'
    ani_key = 'ani:{}'

    def get_ani(self, vid=None, *args):
        """"""
        vid_list = []
        if vid is not None:
            vid_list.append(aid)
        vid_list = vid_list + list(args)
        rds_key_list = list(map(self.ani_key.format, vid_list))
        try:
            res = self.rds.mget(rds_key_list)
        except RedisError:
            logging.error(msg='RedisError: MGET {}'.format(
                rds_key_list), exc_info=True)
            return {}
        return dict([(i.get('video_id'), i) for i in map(json.loads, map(self.byte_decode, filter(None, res)))])

    # ---------- 歌曲信息缓存操作 ----------
    def cache_music(self, data):
        """缓存一首歌的信息到redis"""
        try:
            self.rds.set(self.music_key.format(data.get('mid')), json.dumps(data))
            return True
        except RedisError:
            logging.error(msg='RedisError: SET {} {}'.format(
                self.music_key.format(data.get('mid')), json.dumps(data)
            ), exc_info=True)
            return False

    def cache_multi_music(self, music_info_list):
        """批量缓存歌曲信息"""
        cache_data = dict(
            [(self.music_key.format(m.get('mid')),
              json.dumps(m)) for m in music_info_list])
        try:
            self.rds.mset(**cache_data)
            return True
        except RedisError:
            logging.error(msg='RedisError: MSET {}'.format(str(cache_data)),
                          exc_info=True)
            return False

    def get_multi_music(self, mid_list):
        """批量获取歌曲信息"""
        rds_key_list = list(map(self.music_key.format, mid_list))
        try:
            res = self.rds.mget(rds_key_list)
        except RedisError:
            logging.error(msg='RedisError: MGET {}'.format(
                rds_key_list), exc_info=True)
            return {}
        # return dict([(i.get('mid'), i) for i in map(json.loads, filter(None, res))])
        return dict([(i.get('mid'), i) for i in map(json.loads, map(self.byte_decode, filter(None, res)))])

    def clear_music(self, mid=None, mid_list=None):
        """清除歌的缓存"""
        del_key = []
        if mid is not None:
            del_key += [self.music_key.format(mid)]
        if mid_list is not None:
            del_key += list(map(self.music_key.format, mid_list))
        if not del_key:
            return True
        try:
            self.rds.delete(*del_key)
            return True
        except RedisError:
            logging.error(msg='RedisError: DEL {}'.format(
                del_key), exc_info=True)
            return False
    # ---------- 歌曲信息缓存操作 ----------

    def byte_decode(self, res):
        """# TODO 在windows下会是bytes，需要处理一下"""
        return bytes.decode(res)