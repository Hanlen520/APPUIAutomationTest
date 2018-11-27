#-*- coding:utf8 -*-
from init.android.demoProject.demoProjectInit import DemoProjectInit

import ConfigParser

def android_init():
    """
    初始化android项目必要的数据
    :return:
    """
    config = ConfigParser.ConfigParser()
    config.read('config/android/android_init.conf')

    if 1==int(config.get('isInit','demoProject')):
        DemoProjectInit().init()
