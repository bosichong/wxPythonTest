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






'''

import wx

class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        #调用父类的创建方法
        super(HelloFrame, self).__init__(*args, **kw)

        hbox = wx.BoxSizer(wx.VERTICAL)
        bt0 = wx.Button(self,1,"wx.Dialog")
        bt1 = wx.Button(self,1,"wx.Dialog")
        bt2 = wx.Button(self,1, 'Error')
        bt3 = wx.Button(self, 1,'Question')
        bt4 = wx.Button(self, 1,'Alert')

        bt0.Bind(wx.EVT_BUTTON, self.onModal0)
        bt1.Bind(wx.EVT_BUTTON,self.onModal1)
        bt2.Bind(wx.EVT_BUTTON, self.showMessage1)
        bt3.Bind(wx.EVT_BUTTON, self.showMessage2)
        bt4.Bind(wx.EVT_BUTTON, self.showMessage3)





        hbox.AddMany([(bt0,1,wx.EXPAND|wx.ALIGN_TOP),(bt1,1,wx.EXPAND),(bt2,1,wx.EXPAND),(bt3,1,wx.EXPAND),(bt4,1,wx.EXPAND),])
        self.SetSizer(hbox)

    def onModal0(self, event):
        '''模态'''
        wx.Dialog(self,1, "Dialog",pos=(100,100)).ShowModal()

    def onModal1(self, event):
        '''无模态'''
        wx.Dialog(self,1, "Dialog",pos=(100,100)).Show()

    def showMessage(self,e):
        smd = wx.MessageDialog(None,"This is a Message Box", "Message" ,wx.YES_NO|wx.YES_DEFAULT | wx.ICON_INFORMATION)
        smd.ShowModal()

    def showMessage1(self, event):
        dial = wx.MessageDialog(None, 'Download completed', 'Info', wx.OK)
        ret = dial.ShowModal()
        if ret==wx.OK:
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
    frm = HelloFrame(None, title='wxPython Button',)
    frm.Show()#显示窗口
    app.MainLoop()#持续更新窗口


if __name__ == '__main__':
        main()