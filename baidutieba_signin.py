# !/user/bin/env python
# -*- coding:utf-8 -*-
# time: 2018/2/27--19:24
# 来源：https://github.com/Henryhaohao/Baidu_Tieba_Signin/
__author__ = 'Henry'

'''
项目:百度贴吧一键签到
目标网址:https://tieba.baidu.com/
内容:实现一键将关注的贴吧全部签到
'''

import requests, re
# 输出日期
from datetime import date
today = str(date.today())
print(today)

def signin():
    print('*' * 30 + '百度贴吧签到小助手' + '*' * 30)
    cookie = '在这填写登录百度贴吧后获取的Cookie值'
    # 例如 cookie = 'xxxxxxxxxxx'
    url = 'https://tieba.baidu.com/'
    headers = {
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    html = requests.get(url, headers=headers).text
    tieba = re.findall(r'forum_name":"(.*?)"', html)
    tieba = tieba[:int(len(tieba) / 2)]
    print('正在进行贴吧签到...')
    num = 0
    for i in tieba:
        i = i.replace('\\\\', '\\').encode('latin-1').decode('unicode_escape')
        url = 'http://tieba.baidu.com/sign/add'
        form = {'ie': 'utf-8',
                'kw': i,  # 要签到的贴吧名
                'tbs': '9da208cc747e7b5b1519730458'}
        html = requests.post(url, data=form, headers=headers).json()
        if html['no'] == 1101:
            print('[' + i + '吧]:' + '亲，此贴吧您之前已经签过了哦!')
        if html['error'] == '' or html['no'] == 0:
            print('[' + i + '吧]:' + '签到成功!')
            num += 1
    print('\n')
    print('恭喜您,贴吧签到成功!一共签到' + str(num) + '个贴吧!')
    
    # 添加将签到结果发送到微信的功能
    # 默认情况下不开启，需要到 iyuu.cn 获取 token 才能使用。
    # 将 token 替换掉下方的 xxxx ，然后下面三行的 # 去掉，就可以开启功能。
    
    
    #report = {'text':'签到了 '+ str(num) + '个贴吧'}
    #wx = requests.get('https://iyuu.cn/IYUUxxxx.send',params=report)
    #print(wx)



if __name__ == '__main__':
    signin()
