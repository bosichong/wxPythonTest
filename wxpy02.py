#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# @Time    : 2018-12-19
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : wxPython编程学习笔记(02)wxPython的布局
# @Url     : http://www.17python.com/blog/88
# @Details : wxPython编程学习笔记(02)wxPython的布局
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm


'''

## wxPython的布局

窗口程序中会用到很多的小部件，有序的排列这些小部件可以让应用更直观，

我们可以选择下列sizers：

1.wx.BoxSizer

2.wx.StaticBoxSizer

3.wx.GridSizer

4.wx.FlexGridSizer

5.wx.GridBagSizer

这里我介绍一下`wx.BoxSizer`，灵活应用它基本上可以满足大部分窗口中的布局。


## wx.BoxSizer

`wx.BoxSizer`有`wx.VERTICAL`或`wx.HORIZONTAL`两种方向属性，而且可以嵌套，这样复杂的窗口布局也可以迎刃解决。

如果我们使用wx.EXPAND标志，我们的部件将使用所有已分配给它的空间。

列举一些属性：

1.wx.LEFT

2.wx.RIGHT

3.wx.BOTTOM

4.wx.TOP

5.wx.ALL

以上属性用来控制小部件在布局管理器中的位置，wx.All 可以用来控制边距，例如：

    vbox.Add(midPan, 1, wx.EXPAND | wx.ALL, 20)

我们还可以通过以下属性定义我们的部件对齐：：

1.wx.ALIGN_LEFT
2.wx.ALIGN_RIGHT
3.wx.ALIGN_TOP
4.wx.ALIGN_BOTTOM
5.wx.ALIGN_CENTER_VERTICAL
6.wx.ALIGN_CENTER_HORIZONTAL
7.wx.ALIGN_CENTER

好了，下边列举了一下小例子：

'''

import wx


class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        # 调用父类的创建方法
        super(HelloFrame, self).__init__(*args, **kw)
        # 创建一个面板窗口，panel 是用来放置各种小部件的面板，通常内置于Frame内部
        pl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)  # 第一行组件

        st = wx.TextCtrl(pl)
        hbox1.Add(st, proportion=1, )

        bt1 = wx.Button(pl, label="hello world")
        hbox1.Add(bt1, )

        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)  # 第二行组件

        bt2 = wx.Button(pl, label="hello world")
        bt3 = wx.Button(pl, label="hello world")
        bt4 = wx.Button(pl, label="hello world")
        hbox2.Add(bt2, wx.EXPAND)
        hbox2.Add(bt3, )
        hbox2.Add(bt4, wx.EXPAND)
        vbox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        sb = wx.StaticBox(pl, label="test")  # 第三行组件
        hbox3 = wx.StaticBoxSizer(sb,wx.HORIZONTAL)

        bt5 = wx.Button(pl, label="yes")
        bt6 = wx.Button(pl, label="no")
        hbox3.Add(bt5, )
        hbox3.Add(bt6, flag=wx.LEFT | wx.BOTTOM, border=10)
        vbox.Add(hbox3, flag=wx.ALIGN_RIGHT | wx.RIGHT| wx.BOTTOM, border=10)

        bt7 = wx.Button(pl,label="hello world")
        vbox.Add(bt7,flag=wx.BOTTOM|wx.CENTER)

        pl.SetSizer(vbox)


def main():
    app = wx.App()
    frm = HelloFrame(None, title='wxPython 布局练习',)
    frm.Show()  # 显示窗口
    app.MainLoop()  # 持续更新窗口


if __name__ == '__main__':
    main()
