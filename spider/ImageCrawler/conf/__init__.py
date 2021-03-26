import os
import configparser

def init_config(conf_file):
    global server_port
    global process_num

    config = configparser.ConfigParser()
    config.read(conf_file)
    server_port = int(config.get('server_conf', 'server_port'))
    process_num = int(config.get('server_conf', 'process_num'))

    conf_redis = parse_redis_config(config)
    RedisClient.init_redis(**conf_redis)
    redis_client.RedisClient().init(**conf_redis)

    conf_mysql = parse_mysql_config(config)
    conf_mysql['db'] = 'wenshu_system'
    db.bind('mysql', **conf_mysql)
    db.generate_mapping(create_tables=True)
    conf_mysql['db'] = 'wenshu_data'
    db_data.bind('mysql', **conf_mysql)
    db_data.generate_mapping(create_tables=True)

    set_stop_words()