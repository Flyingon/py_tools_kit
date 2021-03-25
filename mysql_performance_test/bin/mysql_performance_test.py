# -*- coding:utf-8 -*-

import pymysql
import time
import random
from functools import wraps

config = {
    'host': '10.101.201.45',
    'port': 3306,
    'database': 'test',
    'user': 'admin-joeeyuan',
    'password': 's%Hx0HE0ZkX#N1X^',
    'charset': 'utf8'
}

conn = pymysql.connect(**config)
cur = conn.cursor()


def get_sql_list_from_file(file_path):
    sql_list = []
    with open(file_path, "r") as f:
        data_list = f.readlines()
        for d in data_list:
            d = d.strip(" ").strip("\n").strip("\r")
            sql_list.append(d)
    return sql_list


def timer(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        seconds = end - start
        print("{func}函数每 {count} 条数数据写入耗时 {sec}秒".format(func=func, count=args[1], sec=seconds))
        return r
    return _wrapper



class MysqlPerformanceTest:

    def __init__(self, sql_list, every_time_nums=1):
        self.sql_list = sql_list
        self.every_time_nums = every_time_nums

    # 普通写入
    @timer
    def sql_execute(self, count, is_random=False):
        for i in range(count):
            sql = self.insert_sql_list[0]
            if is_random:
                sql = random.choice(self.insert_sql_list)
            cur.execute(sql)

    # 事务处理
    @timer
    def transaction_insert(self, count, is_random=False):
        sql = self.insert_sql_list[0]
        if is_random:
            sql = random.choice(self.insert_sql_list)
        if count > 0:
            try:
                for i in range(count):
                    cur.execute(sql)
            except Exception as e:
                conn.rollback()  # 事务回滚
                print('事务处理失败', e)
            else:
                conn.commit()  # 事务提交
                print('事务处理成功, 关闭连接', cur.rowcount)
                cur.close()
                conn.close()
        else:
            print("输入的count有问题，无法执行数据库操作！")


def test_insert(count):
    insert_sql_list = get_sql_list_from_file("../file/insert_100.sql")
    select_sql_list = get_sql_list_from_file("../file/select_100.sql")
    mysql_performance_test = MysqlPerformanceTest(insert_sql_list, select_sql_list)
    mysql_performance_test.ordinary_insert(count)
    mysql_performance_test.many_insert(count, 20)
    mysql_performance_test.transaction_insert(count)


if __name__ == '__main__':
    test_insert(100)
