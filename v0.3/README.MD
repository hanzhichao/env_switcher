# 饿了么/美团/百度外卖 三方平台 测试/预发环境切换器

> author: Han zhichao
> version 0.2
> finish date: 2018/1/23

## 使用方法

1. 切换所有平台到测试环境 http://localhost:5000/api/switch_env/
2. 切换所有平台到预发环境 http://localhost:5000/api/switch_env/?env=pre
3. 切换某个平台到某个环境环境  http://localhost:5000/api/switch_env/?env=pre&platform=baidu