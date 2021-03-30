# -*- coding: UTF-8 -*-
import sys
import logging
import requests
import time

req_url = "http://zjj.sz.gov.cn:8004/api/marketInfoShow/getEsfCjxxGsData"

dft_headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Content-Length": "0",
    "Host": "zjj.sz.gov.cn:8004",
    "Origin": "http://zjj.sz.gov.cn:8004",
    "Referer": "http://zjj.sz.gov.cn:8004/marketInfoShow/Esfcjxxgs.html",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
}

proxies = {
    'http': 'http://127.0.0.1:12639',
    'https': 'http://127.0.0.1:12639',
}

def get_second_handler_data(mill_ts):
    headers = dft_headers
    headers["Referer"] = dft_headers["Referer"] + "?t=%s" % mill_ts
    r = requests.post(url=req_url + "?t=%s" % mill_ts, json={}, headers=headers, timeout=3, proxies=proxies)
    print(r.status_code)
    print(r.text)


if __name__ == '__main__':
    mill_ts = int(time.time() * 1000)
    mill_ts = 1616910111000
    print(mill_ts)

    get_second_handler_data(mill_ts)
