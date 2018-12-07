#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 19:39
# @Author  : Geng zhi
# @File    : w3c-Python-Spider-06.py


# 网站保持登陆的机制
# 1)cookies机制：本地浏览器保存登陆站点的个人信息
# 2)session机制: 基于会话管理,而cookie就充当会话中的ID用于服务器识别用户每次请求会话


# cookies
'''
cookies举例：
可以从chrome浏览器中查看：
Cookie: bid=pXQHIu1X9xw; douban-fav-remind=1; __utmv=30149280.5677; __yadk_uid=AX36qmT97ELsJsvvfR8fagjqIi2syMjb; gr_user_id=26b80fea-31ad-4a4f-b52a-410b2c18540a; _vwo_uuid_v2=DEADA732392D63FD87E3ED1D6F221C50F|3ae4b3a22e7f527ba6d688a9ec30fa9b; viewed="26381341_27108677"; push_noty_num=0; push_doumail_num=0; ll="108288"; __utmc=30149280; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1544096764%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DJVr4Bw2AVBShpwGZAqtgWRoVg1G71HhJpc8cU7JrpjKtdmVbgqBHYuF4idt249Gk%26wd%3D%26eqid%3D9d2cf11100040023000000035c090bf7%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1734537848.1536767190.1543936396.1544096764.16; __utmz=30149280.1544096764.16.15.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; dbcl2="56777147:h0d1MYuxy7A"; _ga=GA1.2.1734537848.1536767190; _gid=GA1.2.1361779119.1544096773; _gat_UA-7019765-1=1; ck=vOFy; _pk_id.100001.8cb4=fceaa03afad78c1a.1536767031.11.1544096774.1543936396.; ap_v=0,6.0; __utmb=30149280.3.10.1544096764
'''

# 注意：cookies中每个分号算一项
cookie = 'bid=pXQHIu1X9xw; douban-fav-remind=1; __utmv=30149280.5677; __yadk_uid=AX36qmT97ELsJsvvfR8fagjqIi2syMjb; gr_user_id=26b80fea-31ad-4a4f-b52a-410b2c18540a; _vwo_uuid_v2=DEADA732392D63FD87E3ED1D6F221C50F|3ae4b3a22e7f527ba6d688a9ec30fa9b; viewed="26381341_27108677"; push_noty_num=0; push_doumail_num=0; ll="108288"; __utmc=30149280; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1544096764%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DJVr4Bw2AVBShpwGZAqtgWRoVg1G71HhJpc8cU7JrpjKtdmVbgqBHYuF4idt249Gk%26wd%3D%26eqid%3D9d2cf11100040023000000035c090bf7%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1734537848.1536767190.1543936396.1544096764.16; __utmz=30149280.1544096764.16.15.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; dbcl2="56777147:h0d1MYuxy7A"; _ga=GA1.2.1734537848.1536767190; _gid=GA1.2.1361779119.1544096773; _gat_UA-7019765-1=1; ck=vOFy; _pk_id.100001.8cb4=fceaa03afad78c1a.1536767031.11.1544096774.1543936396.; ap_v=0,6.0; __utmb=30149280.3.10.1544096764'

# 我们来处理一下cookies
def cookies_regular(cookie):
    coo = {}
    for item in cookie.split(';'):
        # 值分割一次，值里边有等号就不再分割了
        k, v = item.split('=', 1)
        # print(k, v)
        # 写入字典
        coo[k.strip()] = v.replace('"', '')
    return coo

my_cookies = cookies_regular(cookie)
print(my_cookies)

import requests

base_url = 'https://www.douban.com/'
# 定义一个headers
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

response = requests.get(base_url, headers=headers, cookies=my_cookies)
print(response.status_code) # 200
# print(response.text)

# 检查响应中有自己的用户名
print('timyl' in response.text)  # True

# 注意：只有登陆状态下才能爬取登陆页面中的内容

print('-------------------------------------------------')
# 使用requests直接登陆一个网站
# 如果说cookies失效时间很快，我们需要经常更新cookies，不是很封边；现在我们直接使用requests来登陆一个site
# 主要是我们在登陆的时候提交的表单数据需要分析出来，例如：
'''
source: index_nav
form_email: gongtixinyi@163.com
form_password: xxxxxxx
'''
# requests的session对象，可以跨请求来保持cookies一致; 只要请求过一次，后续的请求可以保证cookies的一致性
s = requests.Session()
print(s.get('https://www.douban.com/')) # <Response [200]>

# 举例：访问httpbin站点并设置cookies值
print(s.get('http://httpbin.org/cookies/set/sessioncookie/12345678900')) # <Response [200]>
print(s.cookies)
# 第二次访问这个网址
print(s.get('http://httpbin.org/cookies').text)
# 结果：可以看到依然保存了我们设置的cookies
'''
{
  "cookies": {
    "sessioncookie": "12345678900"
  }
}
'''

# 使用requests来实现登陆豆瓣------------
import requests
from lxml import etree

# 定义session对象
s = requests.Session()

# 构造post表单, 登陆页面URL，和headers
data = {'source': 'index_nav', 'form_email': 'gongtixinyi@163.com', 'form_password': 'cisco123---'}
login_url = 'https://www.douban.com/accounts/login/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

# 提交数据,返回值res其实就是个人主页
# res = s.post(login_url, data=data, headers=headers)

# print('timyl' in res.text) # True
# print(res.text)

# 注意：连续登陆多次网站就会有保护机制了，例如"验证码"登陆
# 带验证码的情况，提交的表单有什么不同呢？
'''
source: index_nav
form_email: gongtixinyi@163.com
form_password: xxxxxxx
captcha-solution: through  (这个就是验证码)
captcha-id: j2nFPsuq26dEwylt2YjC2k4f:en  (这个id是个变量，每次都不一样，我们可以从登陆页面的源码中搜索到，可以解析到)
'''
# 所以我们的策略就是：验证码(可以使用第三方库来识别)，id用解析的方式来获取，然后接着在根上边三项来绑定到一个表单中提交
# 1）
s1 = requests.Session()
log_url = 'https://www.douban.com/login'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

response1 = s1.get(log_url, headers=headers)

# 1) 验证码的获取---------------------
# 获取验证码图片的链接
selector = etree.HTML(response1.text)
cap_url = selector.xpath('//*[@id="captcha_image"]/@src')[0]
print(cap_url)
cap_img = requests.get(cap_url)

# 引入PIL包(python3.7中叫Pillow)，处理图片;
from PIL import Image
from io import BytesIO

# 这里我们使用Image函数打开，然后内部使用BytesIO函数来打开二进制的图片，最后使用img.show()方法显示
img = Image.open(BytesIO(cap_img.content))
# print(type(img)) # <class 'PIL.JpegImagePlugin.JpegImageFile'>
print(img.show())

# 有了验证码，我们就可以写一个手工的提示输入框，来提示爬虫操作人员输入相应的验证码，即可
cap_text = input('清输入你看到的验证码:')

# 2) captcha-id的获取------------------
# 注意：其实仔细观察，这个id在image的链接中也包含了，不用在网页中重新使用xpath解析了
# 例如：src="https://www.douban.com/misc/captcha?id=jWB44NiLoxKTgKwe5pWTZ1Ly:en&amp;size=s"
cap_id = cap_url.split('=')[1].split('&')[0]
# print(cap_id)

# 3) 开始构造表单
# 构造之前，我们再确认下登陆页面，表单内容
'''
source: None
redir: https://www.douban.com
form_email: gongtixinyi@163.com
form_password: cisco123---
captcha-solution: stitch
captcha-id: mgsLBkCUQh2eWKGtKI2hS5dZ:en
login: 登录
'''
# 注意后边的cap_text 和 cap_id变量
data1 = {'source': 'index_nav', 'form_email': 'gongtixinyi@163.com', 'form_password': 'cisco123---', 'captcha-solution': cap_text, 'captcha-id': cap_id}


# 4) post我们的表单
p = s1.post(log_url, data=data1, headers=headers)
print(p.text)


