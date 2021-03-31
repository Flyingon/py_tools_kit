# -*- coding: utf-8 -*-
import sys
import time
import json
import threading
import queue
import redis
import random
from collections import OrderedDict


class PerformanceTask:
    def __init__(self, work, max_threshold=1000):
        self.work = work
        self.msg_queue = queue.Queue()
        self.ori_result = []
        self.max_threshold = max_threshold
        self.test_cost = -1

    def one_task(self):
        start = int(time.time() * 1000)
        msg = {
            "cost": -1,
            "res": None,
            "err": None,
        }
        try:
            msg["res"] = self.work()
        except Exception as e:
            msg["err"] = type(e)
        msg["cost"] = int(time.time() * 1000) - start
        self.msg_queue.put(msg)
        return

    def run_multi_thread(self, num):
        self.msg_queue = queue.Queue()
        threads = []
        start = int(time.time() * 1000)
        print("run_multi_thread[%s] begin" % num)
        for i in range(num):
            t = threading.Thread(target=self.one_task)
            threads.append(t)
            t.start()
        # 等待所有线程任务结束。
        for t in threads:
            t.join()
        print("run_multi_thread[%s] end" % num)
        self.test_cost = int(time.time() * 1000) - start

    def show_result(self):
        self.ori_result = []
        slow_result = []
        total = 0
        total_cost = 0
        cost_dis_num = OrderedDict()
        cost_dis_total = OrderedDict()
        while not self.msg_queue.empty():
            msg = self.msg_queue.get()
            #             print(msg)
            cost = msg["cost"]
            threshold = int(cost / 100)
            #             print(cost, threshold)
            if not cost_dis_num.get(threshold):
                cost_dis_num[threshold] = 0
            if not cost_dis_total.get(threshold):
                cost_dis_total[threshold] = 0
            cost_dis_num[threshold] += 1
            cost_dis_total[threshold] += cost
            total += 1
            total_cost += cost
            if cost > self.max_threshold:
                slow_result.append(msg)
            self.ori_result.append(msg)
        print("-" * 20, "分布", "-" * 20)
        print("总数: %s, 总耗时: %s, 请求平均耗时: %s ms, qps: %s"
              % (total, self.test_cost, int(total_cost / total), total / (self.test_cost / 1000)))
        for t in cost_dis_num:
            print("%s-%s: %s %s" % (t * 100, t * 100 + 100, cost_dis_num[t], int(cost_dis_total[t] / cost_dis_num[t])))
        print("-" * 20, "慢请求", "-" * 20)
        print("总数:", len(slow_result))
        for d in slow_result:
            print(d)
