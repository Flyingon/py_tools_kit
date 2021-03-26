# -*- coding: UTF-8 -*-
import json
import requests
from urllib.parse import urljoin
import logging

ins_url = "http://www.insstar.cn/"

def get_data(index):
    ret = None
    url = urljoin(ins_url, index)
    res = requests.post(url)
    if res.status_code == 200:
        try:
            ret = res.json()
        except json.decoder.JSONDecodeError as e:
            logging.error("status_code: %s/n text: %s" % (res.status_code, res.text))
            raise e
    else:
        logging.error("status_code: %s/n text: %s" % (res.status_code, res.text))
    return ret

def parse_result(data):
    ret = {}
    ret["count"] = data["count"]
    ret["id"] = data["id"]
    ret["name"] = data["name"]
    ret["next"] = data["next"]
    ret["page_info"] = data["page_info"]
    ret["top_posts"] = data["top_posts"]
    return ret

def get_page_by_cursor(cursor_id):
    res = get_data(cursor_id)
    print(res)
    data = parse_result(res)
    return data
