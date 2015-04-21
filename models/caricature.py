# -*- coding: utf-8 -*-

__author__ = 'awang'

'''
##表结构
###caricature
| 字 段 | 类 型 | 为 空 | 主 键 | 自 增 | 默认值 | 说 明 | 备 注 |
| ---- |:----:|:----:|:-----:|:----:|:-----:|:----:| ---- |
| id | int(16) | NOT NULL | PRIMARY KEY | AUTO_INCREMENT |  |  |  |
| part_id | int(16) | NOT NULL |  |  |  |  |  |
| name | char(128) | NOT NULL |  |  |  |  |  |
| image_id | int(16) | NOT NULL |  |  |  |  |  |
| image_uri | char(128) | NOT NULL |  |  |  |  |  |
| artist | char(128) |  |  |  | NULL |  |  |
| upload_ip | char(64) | NOT NULL |  |  |  |  |  |
| upload_time | int() | NOT NULL |  |  |  |  |  |
| create_time | int() | NOT NULL |  |  |  |  |  |

'''

from sqlalchemy import Column, Integer, String
from models.dao import Base


class Caricature(Base):
    """ORM结构，如果你了解Django，你很容易明白，如果你不了解，我只能呵呵了。
    到 http://docs.sqlalchemy.org/ 去看看吧
    这里存的是一张张的画
    """
    __tablename__ = 'caricature'

    id = Column(Integer, primary_key=True, index=True)
    part_id = Column(Integer, index=True, nullable=False)
    name = Column(String(50), nullable=False)
    image_id = Column(Integer, index=True, nullable=False)
    image_uri = Column(String(128), nullable=False)
    artist = Column(String(50), nullable=False)

