# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'awang'

import logging


class OPError(Exception):
    """
    20000 ：正常，无报错
    """
    error_dict = {
        20001: 'Argument Missing: {} {}',
        20002: 'Argument Error: {} {}',
        20003: 'Argument ValueError: {} {}',
        20004: 'Argument TypeError: {} {} ',
        20005: 'Argument LengthError: {} {}',
        20101: 'SQLAlchemyError: {} {}',
        20102: 'RedisError: {} {}',
        20103: 'Music NotExists: {} {}',
        20104: 'DataError: multi mid exists: {}, please connect administrator {}',
        20105: 'MediaIdError: {} {}',
        20201: '{} {}',
    }

    def __init__(self, code=None, msg=None, **data):
        """data包含：code=None, msg=None, arg=None, typ=None, val=None"""
        self.code = code  # data.get('code' or '')
        self.msg = msg  # data.get('msg' or '')
        if data:
            self.data = str(data)
        else:
            self.data = ''
        self.message = self.get_msg()

    def get_msg(self):
        """code错误或空的时候，会导致从error_dict里面获取一个None，None不能用来format，
        会报 AttributeError ，需要把这个记下来。
        没有获取到正确的msg，就返回传进来的msg，没有传msg，就返回''
        可以看到上面的error_dict里面有用到format，format的参数不一样，这是没有问题的。
        要保证你的顺序，不然会返回错误的msg给你想要raise的地方。 (*_*)
        """
        try:
            self.msg = self.error_dict.get(self.code).format(
                self.msg, self.data)
        except AttributeError:
            logging.info(msg='Missing code for OPError')
        return self.msg


