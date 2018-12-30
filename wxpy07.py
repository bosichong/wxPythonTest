#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# @Time    : 2018-12-24
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : wxPython编程学习笔记(06)wxPython dialogs 弹出对话框
# @Url     : http://www.17python.com/blog/93
# @Details : wxPython编程学习笔记(06)wxPython dialogs 弹出对话框
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm


'''

## wxPython dialogs 弹出对话框

程序中经常会遇到弹出对话框询问操作的场景，wxPython dialogs为此提供了应用的支持，
wxPython dialogs有几种，常用的比如：wx.MessageBox wx.MessageDialog wx.Dialog wx.adv.AboutBox等。

## dialog的创建

一般dialog都会配合Button使用，当按钮绑定事件后，在绑定事件的函数中创建应用即可，代码如下：

    wx.MessageDialog(None, 'Download completed', 'Info', wx.OK)

其它类型的Dialog创建也类似如下代码，其中风格参数如下：

    flag	meaning
    wx.OK	show OK button
    wx.CANCEL	show Cancel button
    wx.YES_NO	show Yes, No buttons
    wx.YES_DEFAULT	make Yes button the default
    wx.NO_DEFAULT	make No button the default
    wx.ICON_EXCLAMATION	show an alert icon
    wx.ICON_ERROR	show an error icon
    wx.ICON_HAND	same as wx.ICON_ERROR
    wx.ICON_INFORMATION	show an info icon
    wx.ICON_QUESTION	show a question icon

可以根据自己的需要进行组合，例如组合YES和NO，yes默认选择，并且加带图标的代码：wx.YES_NO|wx.YES_DEFAULT | wx.ICON_INFORMATION

## MessageDialog 获取返回值

当点击对话框上的按钮后窗口就会关闭，我们需要获得关闭后的返回值，可以通过如下代码获得：

        dial = wx.MessageDialog(None, 'Are you sure to quit?', 'Question',
            wx.YES_NO | wx.YES_DEFAULT | wx.ICON_QUESTION)
        ret = dial.ShowModal()
        if ret == wx.ID_YES:
            print("YES")
        else:
            print("NO")

好啦，完整的代码在下边，大家可以跑跑看看。

## Dialog和窗口间传递数据

遇到过一个在主窗口弹出Dialog的需求，因为是第一次用wxPython，所以不知道数据如何传送给主窗口，后来网上扒了扒发现了一些答案。
我这里的解决方案：

1. 先在Dialog窗口中创建类属性，然后通过类属性传递给主窗口
2. Dialog中创建一个属性self.ret=0，当点击按钮的时候设置其值为1，这样判断一下这个值，用来接收数据，如果为0就不接收。

具体可以参考下边的代码






'''

import wx


class MyDialog(wx.Dialog):
    def __init__(self, *args, **kw):
        super(MyDialog, self).__init__(*args, **kw)
        self.ret = 0
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.st = wx.TextCtrl(self, wx.ID_ANY, "111")
        self.bt = wx.Button(self, wx.ID_ANY, "提交数据")
        self.bt.Bind(wx.EVT_BUTTON,self.onButton)
        hbox.AddMany([(self.st),(self.bt)])
        self.SetSizer(hbox)

    def onButton(self,e):
        self.ret=1
        self.EndModal(1)

class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        # 调用父类的创建方法
        super(HelloFrame, self).__init__(*args, **kw)

        hbox = wx.BoxSizer(wx.VERTICAL)
        bt0 = wx.Button(self, 1, "wx.Dialog")
        bt1 = wx.Button(self, 1, "wx.Dialog")
        bt2 = wx.Button(self, 1, 'Error')
        bt3 = wx.Button(self, 1, 'Question')
        bt4 = wx.Button(self, 1, 'Alert')

        bt0.Bind(wx.EVT_BUTTON, self.onModal0)
        bt1.Bind(wx.EVT_BUTTON, self.onModal1)
        bt2.Bind(wx.EVT_BUTTON, self.showMessage1)
        bt3.Bind(wx.EVT_BUTTON, self.showMessage2)
        bt4.Bind(wx.EVT_BUTTON, self.showMessage3)

        hbox.AddMany([(bt0, 1, wx.EXPAND | wx.ALIGN_TOP), (bt1, 1, wx.EXPAND), (bt2, 1, wx.EXPAND), (bt3, 1, wx.EXPAND),
                      (bt4, 1, wx.EXPAND), ])
        self.SetSizer(hbox)

    def onModal0(self, event):
        '''模态'''
        myDialog= MyDialog(None, 22, title="Dialog")
        myDialog.ShowModal()
        if myDialog.ret == 1:
            print(myDialog.st.GetValue())
        else:
            print("888888")
        myDialog.Destroy()

    def onModal1(self, event):
        '''无模态'''
        wx.Dialog(self, 1, "Dialog", pos=(100, 100)).Show()

    def showMessage(self, e):
        smd = wx.MessageDialog(None, "This is a Message Box", "Message",
                               wx.YES_NO | wx.YES_DEFAULT | wx.ICON_INFORMATION)
        smd.ShowModal()

    def showMessage1(self, event):
        dial = wx.MessageDialog(None, 'Download completed', 'Info', wx.OK)
        ret = dial.ShowModal()
        if ret == wx.OK:
            print("OK")

    def showMessage2(self, event):
        dial = wx.MessageDialog(None, 'Are you sure to quit?', 'Question',
                                wx.YES_NO | wx.YES_DEFAULT | wx.ICON_QUESTION)
        ret = dial.ShowModal()
        if ret == wx.ID_YES:
            print("YES")
        else:
            print("NO")

    def showMessage3(self, event):
        dial = wx.MessageBox('Download completed', 'Info',
                             wx.OK | wx.ICON_INFORMATION)
        ret = dial
        if ret == wx.OK:
            print("OK")


def main():
    app = wx.App()
    frm = HelloFrame(None, title='wxPython Button', )
    frm.Show()  # 显示窗口
    app.MainLoop()  # 持续更新窗口


if __name__ == '__main__':
    main()
