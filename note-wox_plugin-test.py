#encoding=utf8
import requests
from bs4 import BeautifulSoup
import webbrowser
from wox import Wox, WoxAPI
from pathlib import Path

CloudStudioDir = Path(r'C:\Users\14049\WordAndStudy\Projects\CloudStudio')
NoteDir = CloudStudioDir / 'Notes'


#用户写的Python类必须继承Wox类 https://github.com/qianlifeng/Wox/blob/master/PythonHome/wox.py
#这里的Wox基类做了一些工作，简化了与Wox通信的步骤。
class Main(Wox):

    def request(self, url):
        #如果用户配置了代理，那么可以在这里设置。这里的self.proxy来自Wox封装好的对象
        if self.proxy and self.proxy.get("enabled") and self.proxy.get(
                "server"):
            proxies = {
                "http":
                "http://{}:{}".format(self.proxy.get("server"),
                                      self.proxy.get("port")),
                "https":
                "http://{}:{}".format(self.proxy.get("server"),
                                      self.proxy.get("port"))
            }
            return requests.get(url, proxies=proxies)
        else:
            return requests.get(url)

    #必须有一个query方法，用户执行查询的时候会自动调用query方法
    def query(self, key):
        key_type = type(key)
        key_str = str(key)

        results = []

        results.append(
            {
                "Title": "this is Title",
                "SubTitle": "this is subTitle",
                "IcoPath": "Images\\icons8_note_25px.png",
                # "JsonRPCAction": {
                #     #这里除了自已定义的方法，还可以调用Wox的API。调用格式如下：Wox.xxxx方法名
                #     #方法名字可以从这里查阅https://github.com/qianlifeng/Wox/blob/master/Wox.Plugin/IPublicAPI.cs 直接同名方法即可
                #     "method": "searchFile",
                #     #参数必须以数组的形式传过去
                #     "parameters": [key],
                #     #是否隐藏窗口
                #     "dontHideAfterAction": False
                # }
            },
            {
                "Title": "type  of key",
                "SubTitle": key_type,
                "IcoPath": "Images\\icons8_note_25px.png",
                # "JsonRPCAction": {
                #     #这里除了自已定义的方法，还可以调用Wox的API。调用格式如下：Wox.xxxx方法名
                #     #方法名字可以从这里查阅https://github.com/qianlifeng/Wox/blob/master/Wox.Plugin/IPublicAPI.cs 直接同名方法即可
                #     "method": "searchFile",
                #     #参数必须以数组的形式传过去
                #     "parameters": [key],
                #     #是否隐藏窗口
                #     "dontHideAfterAction": False
                # }
            },
            {
                "Title": "str of key",
                "SubTitle": key_str,
                "IcoPath": "Images\\icons8_note_25px.png",
                # "JsonRPCAction": {
                #     #这里除了自已定义的方法，还可以调用Wox的API。调用格式如下：Wox.xxxx方法名
                #     #方法名字可以从这里查阅https://github.com/qianlifeng/Wox/blob/master/Wox.Plugin/IPublicAPI.cs 直接同名方法即可
                #     "method": "searchFile",
                #     #参数必须以数组的形式传过去
                #     "parameters": [key],
                #     #是否隐藏窗口
                #     "dontHideAfterAction": False
                # }
            })

        return results

    #以下代码是必须的
    if __name__ == "__main__":
        Main()
