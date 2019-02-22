import os,string    #os处理批处理  #StringVar要用    字符串钩子
from tkinter import *    #UI库
from tkinter import messagebox  #消息弹出

#初始值
HostAddress="C:\Windows\System32\drivers\etc\hosts"   #host文件地址
HostReduction='''
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host
# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost
'''

#函数
def AddDomain():
    str=time.get()
    hosts=open(HostAddress,"a+")
    hosts.writelines("\n0.0.0.0    "+str)
    hosts.close()
    messagebox.showinfo(title="状态信息", message="添加屏蔽域名"+str+"成功！")

def cancel():
    str = time.get()
    hosts = open(HostAddress, "r+")
    lines=hosts.readlines()
    hosts.seek(0)
    context = hosts.read()
    for line in lines:
        if line.find(str) != -1:  #遍历多次 防止用户多次添加而不能完全清除
            context = context.replace(line, "")   #获取包含域名的行内容 防止该域名为用户自行添加而无法识别
    hosts.close()
    hosts=open(HostAddress, "w")
    hosts.write(context)
    # hosts.write(HostReduction)
    hosts.close()
    messagebox.showinfo(title="状态信息", message="取消屏蔽域名"+str+"成功！")

def reduction():  #还原host
    hosts = open(HostAddress, "w")
    hosts.write(HostReduction)
    hosts.close()
    messagebox.showinfo(title="状态信息", message="还原host成功！")

def OpenHost():   #打开host文件
    os.system("notepad "+HostAddress)

#构建UI界面
soft=Tk()
soft.title("广告域名屏蔽")
soft.geometry("250x150+885+465")
soft.resizable(0, 0)
text1=Label(soft,text="请输入域名：",compound="center").grid(row=0,column=0,columnspan=2,padx=0,pady=0)
time=StringVar()
time.set("1")
text2=Entry(soft,textvariable=time,width=30).grid(row=1,column=0,columnspan=2,padx=5,pady=0)
button1=Button(soft,text="添加屏蔽",command=AddDomain,width=15).grid(row=2,column=0,padx=5,pady=10)
button2=Button(soft,text="取消屏蔽",command=cancel,width=15).grid(row=2,column=1,padx=5,pady=10)
button3=Button(soft,text="查看host",command=OpenHost,width=15).grid(row=3,column=0,padx=5,pady=10)
button4=Button(soft,text="还原host",command=reduction,width=15).grid(row=3,column=1,padx=5,pady=10)
soft.mainloop()