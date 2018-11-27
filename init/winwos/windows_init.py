#-*- coding:utf8 -*-
from init.winwos.demoPorject.demoProjectInit import DemoProjectInit

import ConfigParser

def windows_init():
    """
    初始化Windows必要的数据
    :return:
    """
    config = ConfigParser.ConfigParser()
    config.read('config/windows/windows_init.conf')

    if 1==int(config.get('isInit','demoProject')):
        DemoProjectInit().init()