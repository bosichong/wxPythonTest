#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# @Time    : 2018-12-18
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : wxPython编程学习笔记(01)Frame程序的窗口
# @Url     : http://www.17python.com/blog/87
# @Details : wxPython编程学习笔记(01)Frame程序的窗口
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm



'''

## 简介

之前的一些小应用都是用的`python tk`来写的，后来发现tk的组件确实有些简单，满足不了程序越来越复杂的界面需求，所以决定学习一下`wxPython`
`wxPython`是一个`Python`包装`wxWidgets`（这是用 C++ 编写），一个流行的跨平台GUI工具包。由Robin Dunn以及Harri Pasanen开发，
`wxPython`是作为一个`Python`扩展模块。

## wxPython的安装

    pip3 install wxPython

如果网络不太好，可以到官网下载进行安装，官方网址：`https://wxpython.org/`

## Frame 窗口

如果我们开始构建一个桌面程序，不妨从一个窗口开始，比如先创建一个`Frame`.

`Wx.Frame (parent, id, title, pos, size, style, name)`

其中的参数含意如下：

Parent 窗口的父类。如果“None”被选择的对象是在顶层窗口。如果“None”未被选择时，所述框显示在父窗口的顶层
id 窗口标识。通常-1为了让标识符自动生成
Title 标题出现在标题栏
Pos 帧(frame)的开始位置。如果没有给出，wxDefaultPosition是由操作系统决定
Size 窗口的尺寸。 wxDefaultSize 是由操作系统决定
style 窗口的外观按样式风格常数控制
name 对象的内部名称


## wxPython hello world

我们通过继承wx.Frame来创建自己的主窗口，然后再构建方法`__init__`中创建窗口中的部件。
`main()`方法中，我们创建一个app，创建一个我们构建的窗口类，就可以展示出来一个窗口了。

怎么样，很简单吧？


'''

import wx

class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        #调用父类的创建方法
        super(HelloFrame, self).__init__(*args, **kw)
        #创建一个面板窗口，panel 是用来放置各种小部件的面板，通常内置于Frame内部
        pl = wx.Panel(self)
        #创建一个静态文本
        st = wx.StaticText(pl,label= "Hello world!!", pos=(20,20))
        font = st.GetFont()
        font.PointSize += 20
        font = font.Bold()
        st.SetFont(font)


def main():
    app = wx.App()
    frm = HelloFrame(None, title='Hello World wxPython 窗口练习')
    frm.Show()#显示窗口
    app.MainLoop()#持续更新窗口


if __name__ == '__main__':
    main()