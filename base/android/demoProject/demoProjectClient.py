# -*- coding:utf-8 -*-
from appium import webdriver
from base.readConfig import ReadConfig
from base.android.demoProject.demoProjectReadConfig import DemoProjectReadConfig
from common.appium.appOperator import AppOperator
class DemoProjectClient(object):

    __instance=None
    __inited=None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance=object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__inited is None:
            self.config = ReadConfig().config
            self.demoProjectConfig = DemoProjectReadConfig().config
            self.driver = webdriver.Remote(self.config.appium_hub,desired_capabilities=self.demoProjectConfig.get_desired_capabilities())
            self.appPerator = AppOperator(self.driver)

            self.__inited=True
