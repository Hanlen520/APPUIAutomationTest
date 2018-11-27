# -*- coding:utf-8 -*-
from pojo.android.demoProject.demoProjectConfig import DemoProjectConfig
import ConfigParser
import os

class DemoProjectReadConfig(object):
    __instance=None
    __inited=None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance=object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__inited is None:
            self.config=self._readConfig('config/android/demoProject/demoProject.conf')
            self.__inited=True

    def _readConfig(self, configFile):
        config = ConfigParser.ConfigParser()
        config.read(configFile)
        demoProjectConfig = DemoProjectConfig()
        demoProjectConfig.platformName = config.get('desired_capabilities','platformName')
        demoProjectConfig.automationName = config.get('desired_capabilities','automationName')
        demoProjectConfig.platformVersion =  config.get('desired_capabilities','platformVersion')
        demoProjectConfig.deviceName = config.get('desired_capabilities','deviceName')
        demoProjectConfig.appActivity = config.get('desired_capabilities','appActivity')
        demoProjectConfig.appPackage = config.get('desired_capabilities','appPackage')
        demoProjectConfig.app =  config.get('desired_capabilities','app')
        # 将安装包所在位置转为绝对路径
        if demoProjectConfig.app:
            demoProjectConfig.app = os.path.abspath(demoProjectConfig.app)
        return demoProjectConfig
