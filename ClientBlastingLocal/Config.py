# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018
@author: 康文洋
"""
from fileOperator import fileOperator

class Config:
    #爆破网址
    LoginUrl = 'http://'
    #验证码URL
    CodeUrl = 'http://'
    #验证码服务API
    ServerAPI = 'http://localhost:9999/api?imgurl='
    #获取Cookie的URL
    CookieURL = 'http://'
    #cookie
    Cookies = ["JSESSIONID=F77639"]
    #Cookie要包含的字段
    CookiesField = ["JSESSIONID"]
    #请求方式
    RequestMethod = 'POST'    # or 'GET'
    #用户账号txt文件
    txt_Username = 'username.txt'  #fileOperator().getCurrentPath+'/username.txt'
    # 用户密码txt文件
    txt_Password = 'password.txt'
    # 是单线程爆破？
    # 对于带验证码的爆破只能使用单线程爆破
    # 如果不带验证，只是爆破口令，可以使用多线程
    IsSingleThread = False
    Thread_Time = 1000    #毫秒
    #如果是多线程
    Multithread_Num = 2
    #结果刷新时间(秒)
    Result_Time = 5
