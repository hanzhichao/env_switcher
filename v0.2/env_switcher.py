#!/bin/env/python
"""饿了么/美团/百度外卖 三方平台 测试/预发环境切换器"""
# coding=utf-8
import sys
import json
import requests

def load(path):
    """加载json文件,:@param path: json文件路径,:return 字典格式"""
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def switch_elm(env='dev'):
    """切换elm环境，默认指向测试环境，传入'pre'参数，切换到预发环境"""
    api = load("api/elm.json")
    if env == 'pre':
        api['data']['params']['pushUrl'] = 'http://test.spicespirit.com/itackaway/TTakeaway/newe'
        api['data']['params']['callBackUrl'] = 'http://test.spicespirit.com/itackaway/TTakeaway/newe'

    res = requests.post(api['uri'], data=json.dumps(api['data']), headers=api['headers'], cookies=api['cookies'])

    if '"error":null' in res.text:
        print("elm switch success")
    else: 
        print(res.text)


def switch_meituan(env='dev'):
    """切换meituan外卖环境，默认指向测试环境，传入'pre'参数，切换到预发环境"""
    api = load("api/meituan.json")
    if env == 'pre':
        api['data']['callback_url'] = "http://test.spicespirit.com/Itackaway/TTakeaway/m"

    res = requests.post(api['uri'], data=api['data'], headers=api['headers'], cookies=api['cookies'])
    
    if '"msg":""' in res.text:
        print("meituan switch success")
    else:
        print(res.text)


def switch_baidu(env='dev'):
    """切换baidu外卖环境，默认指向测试环境，传入'pre'参数，切换到预发环境"""
    api = load("api/baidu.json")
    if env == 'pre':
        api['data']['push_url'] = "http://test.spicespirit.com/Itackaway/TTakeaway/b"

    res = requests.post(api['uri'], data=api['data'], headers=api['headers'], cookies=api['cookies'])

    if '"errno":0' in res.text:
        print("baidu switch success")
    else:
        print(res.text)

def switch(env='dev', platform=None):
    """切换环境，默认指向测试环境，传入'pre'参数，切换到预发环境, platform = 'elm'/'meituan'/'baidu'"""
    if not platform:
        switch_elm(env)
        switch_meituan(env)
        switch_baidu(env)
    elif platform == 'elm':
        switch_elm(env)
    elif platform == 'meituan':
        switch_meituan(env)
    elif platform == 'baidu':
        switch_baidu(env)
    else:
        print("platform args wrong")


if __name__ == '__main__':
    n = len(sys.argv) -1
    if n == 0:
        switch()
    elif n == 1:
        switch(sys.argv[1])
    else:
        switch(sys.argv[1], sys.argv[2])
