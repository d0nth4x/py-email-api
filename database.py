import configparser
import mysql.connector


def mysqlConfig(config, name='mysql'):
    ret = {}
    if config.has_section(name):
        items = config.items(name)
        for item in items:
            ret[item[0]] = item[1]
    else:
        raise Exception('Config: nie znaleziono sekcji {0}'.format(name))

    return ret

config = configparser.ConfigParser()
config.read_file(open('emailapi.cfg'))
appDb = mysqlConfig(config)
