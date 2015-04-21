# -*- coding: utf-8 -*-

__author__ = 'awang'

'''
##表结构
###music
| 字 段 | 类 型 | 为 空 | 主 键 | 自 增 | 默认值 | 说 明 | 备 注 |
| ---- |:----:|:----:|:-----:|:----:|:-----:|:----:| ---- |
| mid | int(16) | NOT NULL | PRIMARY KEY | AUTO_INCREMENT |  |  |  |
| name | char(256) | NOT NULL |  |  |  |  |  |
| music_uri | char(128) | NOT NULL |  |  |  |  |  |
| lyrics | text() | NULL |  |  |  |  |  |
| artist | char(128) | NOT NULL |  |  |  |  |  |
| lyricist | char(128) | NULL |  |  |  |  |  |
| composer | char(128) | NULL |  |  |  |  |  |
| producer | char(128) | NULL |  |  |  |  |  |
| arranger | char(128) | NULL |  |  |  |  |  |
| isrc | char(32) |  |  |  | NULL |  |  |
| create_time | int() | NOT NULL |  |  |  |  |  |
'''

from sqlalchemy import Column, Integer, String, Text
from models.dao import Base


class Music(Base):
    """音乐基础表结构
    """
    __tablename__ = 'music'

    mid = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    lyrics = Column(Text, default='')
    music_uri = Column(String(100), nullable=False)
    artist = Column(String(50), nullable=False)
    lyricist = Column(String(50), default='')
    composer = Column(String(50), default='')
    producer = Column(String(50), default='')
    arranger = Column(String(50), default='')
    isrc = Column(String(20), default='')
    create_time = Column(Integer, nullable=False, index=True, default=0)
