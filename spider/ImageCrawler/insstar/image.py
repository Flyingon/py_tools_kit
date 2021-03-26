# 图片下载和保存
# -*- coding: UTF-8 -*-
import requests
import os
import logging

PIC_DIR = "./pic"


def get_pic(source_url):
    resp = requests.get(source_url)
    if resp.status_code != 200:
        return None
    return resp.content


def save_pic(img, pic_path):
    with open(pic_path, 'wb') as fp:
        fp.write(img)


def gen_path(index_id):
    index_path = os.path.join(PIC_DIR, index_id)
    if not os.path.exists(index_path):
        logging.info("path[%s] is not existed, create", index_path)
        os.mkdir(index_path)
    return index_path


def down_pic(index_id, pic_code, source_url):
    path = gen_path(index_id)
    pic_name = "%s.jpg" % pic_code
    pic_path = os.path.join(path, pic_name)
    if os.path.exists(os.path.join(pic_path)):
        return None, pic_path
    img = get_pic(source_url)
    if not img:
        err_msg = "get pic none, source_url: %s", source_url
        logging.error(err_msg)
        return err_msg, pic_path
    save_pic(img, pic_path)
    return None, pic_path
