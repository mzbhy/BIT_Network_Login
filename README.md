# BIT_Network_Login
用于北理工网络认证的简单脚本

脚本用python2.7.10编写，利用urllib和urllib2获取URLs(Uniform Resource Locators)数据，利用cookielib处理cookie(校园网登录不需要)

## 使用方法

```bash
git clone https://github.com/lxalxy/BIT_Network_Login.git
cd BIT_Network_Login
```

修改脚本内data中的yourid和yourpassword为自己的上网账号和密码

```bash
python BIT_Log_In.py
```
## 2016.12.07更新

利用docopt添加命令行运行方式

首先需要安装docopt

```bash
sudo pip install docopt
```

Usage:

```bash
BIT_Log_In_CLI  <ID> <password>
```

Options:
```bash
-h,--help        显示帮助菜单
```

Example:
```bash
python BIT_Log_In_CLI.py yourid yourpassword
```

## To Do

解决docopt在Windows CMD下帮助菜单乱码问题