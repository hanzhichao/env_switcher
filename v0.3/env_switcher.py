#!/bin/env/python
# coding=utf-8
"""饿了么/美团/百度外卖 三方平台 测试/预发环境切换器"""
import sys
import json
import requests
import platform
from threading import Thread

if (platform.python_version()) < '3':
    import codecs.open as open

def load(path):
    """加载json文件,:@param path: json文件路径,:return 字典格式"""
    if (platform.python_version()) < '3':
        with codes.open(path, encoding='utf-8') as f:
            return json.load(f)
    else:
        with open(path, encoding='utf-8') as f:
            return json.load(f)

def thread(func):
    def wrapper(*args, **kwargs):
        if not args or kwargs:
            t = Thread(target=func)
        elif args:
            t = Thread(target=func, args=args)
        elif kwargs:
            t = Thread(target=func, args=kwargs)
        t.start()
        return func
    return wrapper


@thread
def switch_elm(env='dev'):
    """切换elm环境，默认指向测试环境，传入'pre'参数，切换到预发环境"""
    api = load("api/elm.json")
    if env == 'pre':
        api['data']['params']['pushUrl'] = 'http://test.spicespirit.com/itackaway/TTakeaway/newe'
        api['data']['params']['callBackUrl'] = 'http://test.spicespirit.com/itackaway/TTakeaway/newe'

    res = requests.post(api['uri'], data=json.dumps(api['data']), headers=api['headers'], cookies=api['cookies'])

    if '"error":null' in res.text:
        return "elm switch success"
    else: 
        return res.text

@thread
def switch_meituan(env='dev'):
    """切换meituan外卖环境，默认指向测试环境，传入'pre'参数，切换到预发环境"""
    api = load("api/meituan.json")
    if env == 'pre':
        api['data']['callback_url'] = "http://test.spicespirit.com/Itackaway/TTakeaway/m"

    res = requests.post(api['uri'], data=api['data'], headers=api['headers'], cookies=api['cookies'])
    
    if '"msg":""' in res.text:
       return "meituan switch success"
    else:
        return res.text

@thread
def switch_baidu(env='dev'):
    """切换baidu外卖环境，默认指向测试环境，传入'pre'参数，切换到预发环境"""
    api = load("api/baidu.json")
    if env == 'pre':
        api['data']['push_url'] = "http://test.spicespirit.com/Itackaway/TTakeaway/b"

    res = requests.post(api['uri'], data=api['data'], headers=api['headers'], cookies=api['cookies'])

    if '"errno":0' in res.text:
        return "baidu switch success"
    else:
        return res.text

def switch(env='dev', platform=None):
    """切换环境，默认指向测试环境，传入'pre'参数，切换到预发环境, platform = 'elm'/'meituan'/'baidu'"""
    if not platform:
        return switch_elm(env) + "<br>" + switch_meituan(env) + "<br>" + switch_baidu(env)
    elif platform == 'elm':
        return switch_elm(env)
    elif platform == 'meituan':
        return switch_meituan(env)
    elif platform == 'baidu':
        return switch_baidu(env)
    else:
        return "platform args wrong"


if __name__ == '__main__':
    pass
