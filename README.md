# [APP UI自动化测试]()
# [概况]()
* 本项目采用UI MAP和Page Object设计模式
* 本项目由pytest、assertpy、selenium、appium、PyMySQL、allure、redis的python模块组成
    * pytest是python的一个单元测试框架,https://docs.pytest.org/en/latest/
    * assertpy是一个包含丰富的断言库,支持pytest,https://github.com/ActivisionGameScience/assertpy
    * selenium是ui自动化测试框架,https://www.seleniumhq.org/
    * appium是移动端的自动化测试框架,https://github.com/appium/appium/tree/v1.9.1
    * PyMySQL用于操作MySQL数据库,https://github.com/PyMySQL/PyMySQL
    * allure用于生成测试报告,http://allure.qatools.ru/

# [使用]()
## 一、环境准备
### 1、脚本运行环境准备
#### 1.1、安装python依赖模块
* pip install -r requirements.txt

#### 1.2、安装allure
* 源安装
    * sudo apt-add-repository ppa:qameta/allure
    * sudo apt-get update 
    * sudo apt-get install allure
    * 其他安装方式：https://github.com/allure-framework/allure2
* 手动安装
    * 下载2.4.1版本:https://github.com/allure-framework/allure2/releases
    * 解压allure-2.4.1.zip
    * 加入系统环境变量:export PATH=/home/john/allure-2.4.1/bin:$PATH

#### 1.3、安装openjdk8
* sudo add-apt-repository ppa:openjdk-r/ppa
* sudo apt-get update
* sudo apt-get install openjdk-8-jdk

#### 1.4、安装Oracle Instant Client
* linux
    * 安装libaio包
        * centos:yum install libaio
        * ubuntu:apt-get install libaio1
    * 配置Oracle Instant Client
        * 下载地址:http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html
        * 下载安装包instantclient-basic-linux.x64-18.3.0.0.0dbru.zip
        * 解压zip包,并配置/etc/profile
            * unzip instantclient-basic-linux.x64-18.3.0.0.0dbru.zip
            * export LD_LIBRARY_PATH=/home/john/oracle_instant_client/instantclient_18_3:$LD_LIBRARY_PATH
        * 中文编码设置
        
            ```python 
            import os
            os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
            ```
* Windows
    * 下载地址:http://www.oracle.com/technetwork/topics/winx64soft-089540.html
    * 下载安装包instantclient-basic-windows.x64-11.2.0.4.0.zip
    * 解压zip包,并配置环境变量
        * 系统环境变量加入D:\instantclient-basic-windows.x64-11.2.0.4.0\instantclient_11_2
        * 配置中文编码,环境变量创建NLS_LANG=SIMPLIFIED CHINESE_CHINA.UTF8  
    * 注意:如果使用64位,python和instantclient都需要使用64位
    
### 2、appium server运行环境准备
### 2.1、安装jdk1.8,并配置环境变量
* export JAVA_HOME=/usr/lib/jvm/jdk8
* export JRE_HOME=${JAVA_HOME}/jre 
* export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
* export PATH=${JAVA_HOME}/bin:$PATH

#### 2.2、安装配置appium server
* 安装appium desktop server
    * 下载appium-desktop-setup-1.8.2.exe
    * 下载地址:https://github.com/appium/appium-desktop/releases
    * 以管理员身份启动服务

* Android环境准备
    * 安装java(JDK),并配置JAVA_HOME=/usr/lib/jvm/jdk8
    * 安装Android SDK,并配置ANDROID_HOME="/usr/local/adt/sdk"
    * 使用SDK manager安装需要进行自动化的Android API版本

* 手机chrome环境准备
    * 确保手机已安装chrome浏览器
    * 下载chrome浏览器驱动：https://chromedriver.storage.googleapis.com/index.html
    * 驱动支持的手机浏览器版本：https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/web/chromedriver.md
    * 在appium desktop上设置驱动的路径

* Windows环境准备
    * 支持Windows10及以上版本
    * 设置Windows处于开发者模式
    * 下载WinAppDriver并安装(V1.1版本),https://github.com/Microsoft/WinAppDriver/releases
    * \[可选\]下载安装WindowsSDK,在Windows Kits\10\bin\10.0.17763.0\x64内包含有inspect.exe用于定位Windows程序的元素信息

* 其他更多配置：https://github.com/appium/appium/tree/v1.9.1/docs/en/drivers

## 二、修改配置
* vim config/config.conf 配置测试信息
* vim config/platform/platform_init.conf 配置需要初始化的项目
* vim config/platform/projectName/projectName.conf 配置测试项目的信息

## 三、运行测试
* cd APPUIAutomationTest/
* python runTest.py --help
* python runTest.py 运行cases目录所有的用例
* python runTest.py -k keyword 运行匹配关键字的用例，会匹配文件名、类名、方法名
* python runTest.py -d dir     运行指定目录的用例，默认运行cases目录

## 四、生成测试报告
* cd APPUIAutomationTest/
* python generateReport.py -p 9080
* 访问地址http://ip:9080
* 在使用Ubuntu进行报告生成时，请勿使用sudo权限，否则无法生成，allure不支持

## 五、项目说明
* 元素的显式等待时间默认为30s
* 封装的显式等待类型支持:page_objects/wait_type.py
* 封装的定位类型支持:page_objects/locator_type.py
* 项目
    * demoProject
        * 例子项目
    
# [项目结构]()
* base 基础请求类
* cases 测试用例目录
* common 公共模块
* config　配置文件
* init 初始化
* logs 日志目录
* output 测试结果输出目录
* packages 程序安装包存放目录
* page_objects 页面元素映射和页面对象 
* pojo 存放自定义类对象
* test_data 测试所需的测试数据目录
* runTest.py 测试运行脚本
* generateReport.py 报告生成脚本

# [编码规范]()
* 统一使用python 2.7
* 编码使用-\*- coding:utf8 -\*-,且不指定解释器
* 所有中文都直接使用字符串，不转换成Unicode，即不是用【u'中文'】编写
* 类/方法的注释均写在class/def下一行，并且用三个双引号形式注释
* 局部代码注释使用#号
* 所有的测试模块文件都以test_projectName_moduleName.py命名
* 所有的测试类都以Test开头，类中方法(用例)都以test_开头
* case对应setup/teardown的fixture统一命名成fixture_[test_case_method_name]
* 每一个模块中测试用例如果有顺序要求，则自上而下排序，pytest在单个模块里会自上而下按顺序执行

# [pytest常用]()
* @pytest.mark.skip(reason='该功能已废弃')
* @pytest.mark.parametrize('key1,key2',[(key1_value1,key2_value2),(key1_value2,key2_value2)])
* @pytest.mark.usefixture('func_name')

# [注意点]()
* 运行pytest时指定的目录内应当有conftest.py，方能在其他模块中使用。@allure.step会影响fixture，故在脚本中不使用@allure.step
* 能用id、name、link(不常变化的链接)定位的，不使用css定位，能使用css定位，不使用xpath定位
* 如需要上传文件到手机或者从手机下载文件，请确保有手机对应目录的读写权限
* 视频录制统一对单个单个case进行，保证录制时间不超过3分钟，且录制文件不要过大，否则会引起手机内存无法存储视频
* 设备屏幕坐标系原点都在最左上角，往右x轴递增，往下y轴递增