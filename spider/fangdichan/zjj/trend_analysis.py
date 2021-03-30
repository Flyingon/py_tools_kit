# -*- coding: UTF-8 -*-
import json
from collections import OrderedDict

"""
{
	"status": 1,
	"msg": "成功",
	"data": {
		"date": ["2021-03-24", "2021-03-25", "2021-03-26", "2021-03-27", "2021-03-28", "2021-03-29"],
		"result": "success",
		"ysfDealArea": [15038.15, 13772.01, 14426.38, 13648.48, 10670.55, 8446.31],
		"ysfTotalTs": [156.0, 148.0, 150.0, 141.0, 102.0, 86.0],
		"esfDealArea": [26341.94, 24220.88, 28714.85, 0.0, 0.0, 27729.63],
		"bigEventCont": [null, null, null, null, null, null],
		"esfTotalTs": [300.0, 278.0, 338.0, 0.0, 0.0, 319.0]
	}
}
"""


def trend_analysis():
    with open("./file/deal_trend.json", "r") as f:
        data = json.load(f)["data"]
    # print(data)
    ret_ys = OrderedDict()
    ret_es = OrderedDict()
    for i, d in enumerate(data["date"]):
        key = d[0:7]
        if not ret_ys.get(key):
            ret_ys[key] = 0
        if not ret_es.get(key):
            ret_es[key] = 0
        ret_ys[key] += int(data["ysfTotalTs"][i])
        ret_es[key] += int(data["esfTotalTs"][i])
    data_print(ret_ys)
    # data_print(ret_es)


def data_print(data):
    row = OrderedDict()
    for k, v in data.items():
        key = k[-2:]
        if not row.get(key):
            row[key] = ""
        row[key] += "\t" + str(v)
    for k, v in row.items():
        print(k, v)


if __name__ == '__main__':
    trend_analysis()
