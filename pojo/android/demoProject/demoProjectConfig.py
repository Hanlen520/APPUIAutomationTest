# -*- coding:utf-8 -*-
class DemoProjectConfig:
    def __init__(self):
        self.platformName = None
        self.automationName = None
        self.platformVersion = None
        self.deviceName = None
        self.appActivity = None
        self.appPackage = None
        self.app = None

    @property
    def platformName(self):
        return self.platformName

    @platformName.setter
    def platformName(self,platformName):
        self.platformName=platformName

    @property
    def automationName(self):
        return self.automationName

    @automationName.setter
    def automationName(self,automationName):
        self.automationName=automationName

    @property
    def platformVersion(self):
        return self.platformVersion

    @platformVersion.setter
    def platformVersion(self,platformVersion):
        self.platformVersion=platformVersion

    @property
    def deviceName(self):
        return self.deviceName

    @deviceName.setter
    def deviceName(self,deviceName):
        self.deviceName=deviceName
    @property
    def appActivity(self):
        return self.appActivity

    @appActivity.setter
    def appActivity(self,appActivity):
        self.appActivity=appActivity

    @property
    def appPackage(self):
        return self.appPackage

    @appPackage.setter
    def appPackage(self,appPackage):
        self.appPackage=appPackage

    @property
    def app(self):
        return self.app

    @app.setter
    def app(self,app):
        self.app=app

    def get_desired_capabilities(self):
        desired_capabilities={}
        desired_capabilities.update({'platformName':self.platformName})
        if self.automationName:
            desired_capabilities.update({'automationName':self.automationName})
        desired_capabilities.update({'platformVersion':self.platformVersion})
        desired_capabilities.update({'deviceName':self.deviceName})
        if self.appActivity and self.appPackage:
            desired_capabilities.update({'appActivity':self.appActivity})
            desired_capabilities.update({'appPackage':self.appPackage})
        if self.app:
            desired_capabilities.update({'app':self.app})
        return desired_capabilities