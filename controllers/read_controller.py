# -*- coding: utf-8 -*-

from controllers.base_controller import BaseController
from models.caricature import Caricature
from models.animation import Animation
from models.music import Music
from sqlalchemy.exc import SQLAlchemyError

__author__ = 'awang'


class ReadCaricature(BaseController):
    """"""
    url = r'/op/car/?'

    def get(self, *args, **kwargs):
        """
        """
        part_id = self.data.get('part_id', 1)
        start = self.data.get('start', 0)
        stop = self.data.get('stop', 10)
        try:
            img_list = self.op_session.query(Caricature).filter_by(part_id=part_id).\
                order_by(Caricature.image_id.desc()).slice(start, stop).all()
            count = self.op_session.query(Caricature).filter_by(part_id=part_id).count()
        except SQLAlchemyError as e:
            self.op_session.rollback()
            self.do_write(code=20101, msg=str(e))
            return
        image_list = [self.pack_img(img) for img in img_list]
        self.do_write(code=20000, image_list=image_list, count=count)


class WatchAnimation(BaseController):
    """"""
    url = r'/op/ani/?'

    def get(self, *args, **kwargs):
        """
        """
        video_id = self.data.get('video_id', 1)
        try:
            pre_list = self.op_session.qeury(Animation.video_id).filter(
                Animation.video_id < video_id).order_by(Animation.video_id.desc()).all()
        except SQLAlchemyError as e:
            self.op_session.rollback()
            pre_list = []
        try:
            next_list = self.op_session.qeury(Animation.video_id).filter(
                Animation.video_id > video_id).order_by(Animation.video_id.desc()).all()
        except SQLAlchemyError as e:
            self.op_session.rollback()
            next_list = []
        ani = self.cache.get_ani(video_id)
        ani_pre_list = self.cache.get_ani(*pre_list)
        ani_next_list = self.cache.get_ani(*next_list)
        # TODO 缓存校验
        self.do_write(code=20000, ani=ani, next_list=ani_next_list,
                      pre_list=ani_pre_list)


class ListenMusic(BaseController):
    """"""
    url = r'/op/music/?'

    def get(self):
        """"""
        try:
            mid_list = self.op_session.query(Music.mid).all()
        except SQLAlchemyError as e:
            self.op_session.rollback()
            self.do_write(code=20101, msg=str(e))
            return
        mid_list = [m[0] for m in mid_list]
        music_dict = self.cache.get_multi_music(mid_list)
        no_cache = [i for i in mid_list if i not in music_dict.keys()]
        if no_cache:
            try:
                music_list = self.op_session.query(Music).filter(
                    Music.mid.in_(no_cache)).all()
            except SQLAlchemyError as e:
                self.op_session.rollback()
                music_list = []
            if music_list:
                music_dict.update(dict([(m.get('mid'), m) for m in map(
                    self.pack_music, music_list)]))
                self.cache.cache_multi_music(music_dict.values())
        self.do_write(code=20000, mid_list=mid_list, music_dict=music_dict)