# BIT_Network_Login
用于北理工网络认证的简单脚本

脚本用python2.7.10编写，利用urllib和urllib2获取URLs(Uniform Resource Locators)数据，利用cookielib处理cookie(校园网登录不需要)

## 使用方法

```bash
git clone git@github.com:lxalxy/BIT_Network_Login.git
cd BIT_Network_Login
```

修改脚本内data中的yourid和yourpassword为自己的上网账号和密码

```bash
python BIT_Log_In.py
```