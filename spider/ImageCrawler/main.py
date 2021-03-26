# -*- coding: UTF-8 -*-
import sys
import getopt
import logging
from insstar.crawler import insstar_crawler

CONF_FILE = ''
LOG_FORMAT = '%(levelname)s %(asctime)s %(filename)s %(funcName)s : %(message)s'


def set_log_level(level):
    llevel = logging.INFO if not level else getattr(logging, level.upper())
    logging.basicConfig(format=LOG_FORMAT, level=llevel)
    print("log init finished, level:", level.upper())


def usage():
    """
    使用说明函数
    """
    print('Usage:', sys.argv[0], '-c conf_file')
    sys.exit(1)


def parse_command_line() -> CONF_FILE:
    if len(sys.argv) < 3:
        usage()
    ret = ''
    opts, args = getopt.getopt(sys.argv[1:], "c:", [])
    for option, value in opts:
        if option == "-c":
            ret = value
    return ret


if __name__ == '__main__':
    set_log_level("debug")
    insstar_crawler()
