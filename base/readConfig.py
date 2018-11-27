# -*- coding:utf-8 -*-
from pojo.config import Config
import ConfigParser

class ReadConfig(object):
    __instance=None
    __inited=None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance=object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__inited is None:
            self.config=self._readConfig('config/config.conf')
            self.__inited=True

    def _readConfig(self, configFile):
        configParser = ConfigParser.ConfigParser()
        configParser.read(configFile)
        config = Config()
        config.appium_hub=configParser.get('appium_server','appium_hub')
        return config
