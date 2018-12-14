#-*- coding:utf8 -*-
import os
import platform
class JavaTool:

    @classmethod
    def getAllJar(cls):
        split_flag=':'
        if 'Windows'==platform.system():
            split_flag=';'
        result=''
        libpath=os.path.join(os.path.abspath('common/java/lib/'),'')
        path=os.walk(libpath)
        for dirpath,dirname,filenames in path:
            for filename in filenames:
                filepath=os.path.join(dirpath,filename)
                result=result+split_flag+filepath
        return result.lstrip(split_flag)
