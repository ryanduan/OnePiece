# -*- coding: utf-8 -*-

__author__ = 'awang'

'''
##表结构
###caricature
| 字 段 | 类 型 | 为 空 | 主 键 | 自 增 | 默认值 | 说 明 | 备 注 |
| ---- |:----:|:----:|:-----:|:----:|:-----:|:----:| ---- |
| video_id | int(16) | NOT NULL | PRIMARY KEY | AUTO_INCREMENT |  |  |  |
| video_uri | char(128) | NOT NULL |  |  |  |  |  |
| name | char(256) | NOT NULL |  |  |  |  |  |
| lang | tinyint(1) | NOT NULL |  |  |  |  |  |
| artist | char(128) |  |  |  | NULL |  |  |
| upload_ip | char(64) | NOT NULL |  |  |  |  |  |
| upload_time | int() | NOT NULL |  |  |  |  |  |
| create_time | int() | NOT NULL |  |  |  |  |  |
'''

from sqlalchemy import Column, Integer, String
from models.dao import Base


class Animation(Base):
    """ORM结构，如果你了解Django，你很容易明白，如果你不了解，我只能呵呵了。
    到 http://docs.sqlalchemy.org/ 去看看吧
    """
    __tablename__ = 'caricature'

    video_id = Column(Integer, primary_key=True, index=True)
    video_uri = Column(String(128), nullable=False)
    name = Column(String(50), nullable=False)
    lang = Column(Integer, nullable=False)
    artist = Column(String(50), nullable=False)
    create_time = Column(Integer, nullable=False, index=True, default=0)