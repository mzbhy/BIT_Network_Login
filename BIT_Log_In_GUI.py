#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
import urllib
import urllib2
import cookielib


class LoginFrame(wx.Frame):
    account = 'yourid'
    password = 'yourpassword'

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "校园网登录".decode('utf-8'), size=(300, 300), style= wx.MINIMIZE_BOX | wx.CAPTION | wx.CLOSE_BOX)
        panel = wx.Panel(self, -1)
        wx.StaticText(panel, -1, "Account:", pos=(30, 80), style=wx.ALIGN_RIGHT)
        wx.StaticText(panel, -1, "Password:", pos=(30, 120), style=wx.ALIGN_RIGHT)
        self.resultText = wx.StaticText(panel, -1, "", pos=(30, 200), style=wx.TRANSPARENT_WINDOW)
        self.accountText = wx.TextCtrl(panel, -1, "", pos=(100, 80))
        self.passwordText = wx.TextCtrl(panel, -1, "", pos=(100, 120), style=wx.TE_PASSWORD)
        self.button = wx.Button(panel, -1, "Log In", pos=(100, 160))
        self.accountText.SetValue(self.account)
        self.passwordText.SetValue(self.password)
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetFocus()
        self.Centre()


    def OnClick(self, event):
        self.account = self.accountText.GetValue()
        self.password = self.passwordText.GetValue()
        result = LogIn(self.account, self.password)
        if result[0:8] == 'login_ok':
            result = '登录成功'
        self.resultText.SetLabel(result.decode('utf-8'))



def LogIn(account, password):
    # 登录页面，用于获取cookie
    hosturl = 'http://10.0.0.55:803/srun_portal_pc.php?ac_id=1&'

    # Post地址
    posturl = 'http://10.0.0.55:803/include/auth_action.php'

    # 处理cookie，在校园网登录中不需要
    # filename = 'FileCookieJar.txt'
    # cj = cookielib.LWPCookieJar(filename)
    # cj.save();
    # cookie_support = urllib2.HTTPCookieProcessor(cj)
    # opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    # urllib2.install_opener(opener)
    # h = urllib2.urlopen(hosturl)

    # header数据，通过抓包获得
    headers = {'Referer': 'http://10.0.0.55:803/srun_portal_pc.php?ac_id=1&',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
               }

    # 构造Post数据，通过抓包获得
    data = {'action': 'login',
            'username': account,
            'password': password,
            'ac_id': '1',
            'save_me': '1',
            'ajax': '1'
            }

    # 对Post数据编码
    data = urllib.urlencode(data)

    request = urllib2.Request(posturl, data, headers)
    response = urllib2.urlopen(request)
    text = response.read()
    #print text[0: text.index(',')]
    return text


if __name__ == '__main__':
    app = wx.App(False)
    frame = LoginFrame()
    frame.Show(True)
    app.MainLoop()
