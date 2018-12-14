#-*- coding:utf8 -*-
import jpype
from common.java.javaTool import JavaTool
class CaptchaRecognitionTool:

    @classmethod
    def captchaRecognition(cls,filePath,language='eng'):
        """

        :param filePath: 图片验证码
        :param language: eng:英文,chi_sim:中文
        :return:
        """

        # 启动jvm......'
        jpype.startJVM(jpype.get_default_jvm_path(), "-ea", "-Djava.class.path=" + JavaTool.getAllJar())
        CaptchaRecognition = jpype.JClass('com.ocr.CaptchaRecognition')
        captchaRecognition = CaptchaRecognition('common/java/lib/tess4j/tessdata/')
        captcha = captchaRecognition.captchaRecognitionWithFile(filePath,language)
        # '关闭jvm......'
        jpype.shutdownJVM()
        return captcha
