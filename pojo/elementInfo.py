#-*- coding:utf8 -*-

class ElementInfo:
    def __init__(self):
        self.locator_type=None
        self.locator_value=None
        self.expected_value=None
        self.wait_type=None
        self.wait_seconds=None
        self.wait_expected_value=None

    @property
    def expected_value(self):
        return self.expected_value

    @expected_value.setter
    def expected_value(self,expected_value):
        self.expected_value=expected_value

    @property
    def locator_type(self):
        return self.locator_type

    @locator_type.setter
    def locator_type(self,locator_type):
        self.locator_type=locator_type

    @property
    def locator_value(self):
        return self.locator_value

    @locator_value.setter
    def locator_value(self,locator_value):
        self.locator_value=locator_value

    @property
    def wait_type(self):
        return self.wait_type

    @wait_type.setter
    def wait_type(self,wait_type):
        self.wait_type=wait_type

    @property
    def wait_seconds(self):
        return self.wait_seconds

    @wait_seconds.setter
    def wait_seconds(self,wait_seconds):
        self.wait_seconds=wait_seconds

    @property
    def wait_expected_value(self):
        return self.wait_expected_value

    @wait_expected_value.setter
    def wait_expected_value(self,wait_expected_value):
        self.wait_expected_value=wait_expected_value