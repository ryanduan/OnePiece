# -*- coding: utf-8 -*-

"""
Description
"""
from sqlalchemy.exc import SQLAlchemyError
from controllers.base_controller import BaseController
from models.caricature import Caricature
from models.animation import Animation
from models.music import Music
import logging
import time

__author__ = 'awang'


class CreateCaricature(BaseController):
    """创建漫画
    """
    url = r'/op/create_car/?'

    def post(self, *args, **kwargs):
        """"""
        data = self.data
        data['create_time'] = int(time.time())
        car = Caricature(**data)
        self.op_session.add(car)
        try:
            self.op_session.commit()
            self.do_write(code=20000)
        except SQLAlchemyError as e:
            self.op_session.rollback()
            logging.error(msg='SQLAlchemyError:', exc_info=True)
            self.do_write(code=20101, msg=str(e))


class CreateAnimation(BaseController):
    """创建动画
    """
    url = r'/op/create_ani/?'

    def post(self, *args, **kwargs):
        """"""
        data = self.data
        data['create_time'] = int(time.time())
        ani = Animation(**data)
        self.op_session.add(ani)
        try:
            self.op_session.commit()
            self.do_write(code=20000)
        except SQLAlchemyError as e:
            self.op_session.rollback()
            logging.error(msg='SQLAlchemyError:', exc_info=True)
            self.do_write(code=20101, msg=str(e))


class CreateMusic(BaseController):
    """创建音乐"""
    url = r'/op/create_music/?'

    def post(self, *args, **kwargs):
        """"""
        data = self.data
        data['create_time'] = int(time.time())
        music = Music(**data)
        self.op_session.add(music)
        try:
            self.op_session.commit()
            self.do_write(code=20000)
        except SQLAlchemyError as e:
            self.op_session.rollback()
            logging.error(msg='SQLAlchemyError:', exc_info=True)
            self.do_write(code=20101, msg=str(e))


