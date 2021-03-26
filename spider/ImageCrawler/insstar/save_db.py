# -*- coding: UTF-8 -*-
from datetime import datetime
import logging
import traceback
from model.sqlite import Session
from model.model_insstar import InsstarIndex, InsstarPage
from insstar.image import down_pic


def down_index(data):
    session = Session()
    data_map = {
        "id": data["id"],
        "name": data["name"],
        "count": data["count"],
        "next": data["next"],
        "has_next_page": data["page_info"]["has_next_page"],
        "end_cursor": data["page_info"]["end_cursor"],
        "update_at": datetime.now()
    }
    _save_data(session, InsstarIndex, data_map, "id")
    session.commit()
    return data["next"]


def down_page(insstar_index_id, data_list):
    session = Session()
    for data in data_list:
        data_map = {
            "insstar_index_id": insstar_index_id,
            "code": data["code"],
            "date": data["date"],
            "caption": data.get("caption"),
            "likes": data["likes"],
            "is_video": data["is_video"],
            "source_url": data["display_src"],
            "update_at": datetime.now()
        }
        err, path = down_pic(data_map["insstar_index_id"], data_map["code"], data_map["source_url"])
        if not err:
            data_map["path"] = path
        _save_data(session, InsstarPage, data_map, "code")
    session.commit()


def _save_data(session, table_ins, data_map, unique_key):
    if not session:
        session = Session()
    modify_data = set()
    try:
        old_data = session.query(table_ins).filter(getattr(table_ins, unique_key) == data_map[unique_key]).first()
        if old_data:
            for k, v in data_map.items():
                if k in "update_at":
                    continue
                if v != getattr(old_data, k):
                    setattr(old_data, k, v)
                    modify_data.add(k)
            if modify_data:
                logging.debug("modify_data: %s", modify_data)
                old_data.update_at = datetime.now()
        else:
            data_map['update_at'] = datetime.now()
            session.add(table_ins(**data_map))
            return 0
    except Exception:
        traceback.print_exc()
        return -1
    return 0
