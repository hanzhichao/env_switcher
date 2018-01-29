# coding=utf-8
import requests
import json


def load(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def switch_elem():
    uri = 'https://open.shop.ele.me/api/invoke?method=ApplicationApIService.updateSandboxEnvironment'
    dev_callback_url = dev_push_url = 'http://dev2.spicespirit.com/itackaway/TTakeaway/newe'
    pre_callback_url = pre_push_url = 'http://test.spicespirit.com/itackaway/TTakeaway/newe'
    # headers = load("elm/headers.json")
    cookies = load("elm/cookies.json")
    data = json.dumps(load("elm/data.json")) % (pre_push_url, pre_callback_url)
    headers = {"Content-type": "application/json",}
    res = requests.post(uri, data=data, headers=headers, cookies=cookies)
    # res = requests.post(uri, data=data, cookies=cookies)
    if '"error":null' in res.text:
        print("success")
    else: 
        print(res.text)


def switch_meituan():
    uri = 'http://developer.waimai.meituan.com/basis/callback/url_edit'
    # headers = load("meituan/headers.json")
    cookies = load("meituan/cookies.json")
    data = dict(load("meituan/data.json"))
    data['callback_url'] = "http://test.spicespirit.com/Itackaway/TTakeaway/m"
    res = requests.post(uri, data=data, cookies=cookies)
    # res = requests.post(uri, data=data, headers=headers, cookies=cookies)
    if '"msg":""' in res.text:
        print("success")
    else:
        print(res.text)

def switch_baidu():
    uri = "http://dev.waimai.baidu.com/dev/account/accountupdate"
    # headers = load("baidu/headers.json")
    cookies = load("baidu/cookies.json")
    data = dict(load("baidu/data.json"))
    data['push_url'] = "http://dev2.spicespirit.com/Itackaway/TTakeaway/b"
    # print(data, type(data))

    # res = requests.post(uri, data=data, headers=headers, cookies=cookies, verify=False)
    res = requests.post(uri, data=data, cookies=cookies)
    if '"errno":0' in res.text:
        print("success")
    else:
        print(res.text)



def switch_weixin():
    uri = "https://mp.weixin.qq.com/advanced/advanced?action=interface&t=advanced/interface&token=1109769733&lang=zh_CN"
    headers = load("weixin/headers.json")
    cookies = load("weixin/cookies.json")
    data = dict(load("weixin/data.json"))
    data['url'] = "http://dev.spicespirit.com/wechat/index/wxmp/wpush"
    # print(data, type(data))

    res = requests.post(uri, data=data, headers=headers, cookies=cookies)
    if '"errno":0' in res.text:
        print("success")
    else:
        print(res.text)



# switch_baidu()
# switch_meituan()
switch_elem()