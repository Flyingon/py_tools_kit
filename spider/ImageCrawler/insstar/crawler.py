# -*- coding: UTF-8 -*-
import time
import json
from insstar.cursor_page import get_page_by_cursor
from insstar.save_db import down_index, down_page

def single_crawler(cursor):
    data = get_page_by_cursor(cursor)
    next = down_index(data)
    if data.get("top_posts"):
        down_page(data["id"], data["top_posts"])
    return next

def insstar_crawler():
    next = "214288771"
    while next:
        try:
            next = single_crawler(next)
        except ConnectionResetError:
            time.sleep(10)
            next = single_crawler(next)
        except json.decoder.JSONDecodeError:
            time.sleep(10)
            next = single_crawler(next)
        if not isinstance(next, str):
            next = str(next)
        print("next: ", next)
