# innstar表结构声明
# -*- coding: UTF-8 -*-
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey

Base = declarative_base()


class InsstarIndex(Base):
    __tablename__ = 'insstar_index'

    id = Column(String(20), primary_key=True)
    name = Column(String(50))
    count = Column(Integer)
    next = Column(Integer)
    has_next_page = Column(Boolean)
    end_cursor = Column(String(50))
    update_at = Column(DateTime)


# 存储爬取的每个图片信息
class InsstarPage(Base):
    __tablename__ = 'insstar_page'
    id = Column(Integer, primary_key=True)
    insstar_index_id = Column(String, ForeignKey('insstar_index.id'))
    code = Column(String(20), unique=True)  # http://www.insstar.cn/p/{code}
    caption = Column(String)
    likes = Column(Integer)
    date = Column(String(20))
    is_video = Column(Boolean)
    source_url = Column(String)  # display_src
    path = Column(String, default=None)
    update_at = Column(DateTime)
