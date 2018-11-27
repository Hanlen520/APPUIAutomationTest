#-*- coding:utf8 -*-

class HttpResponseResult():
    def __init__(self):
        self.status_code=None
        self.body=None
        self.cookies=None
        self.headers=None

    @property
    def status_code(self):
        return self.status_code

    @status_code.setter
    def status_code(self,status_code):
        self.status_code=status_code

    @property
    def body(self):
        return self.body

    @body.setter
    def body(self,body):
        self.body=body

    @property
    def cookies(self):
        return self.cookies

    @cookies.setter
    def cookies(self,cookies):
        self.cookies=cookies

    @property
    def headers(self):
        return self.headers

    @headers.setter
    def headers(self,headers):
        self.headers=headers