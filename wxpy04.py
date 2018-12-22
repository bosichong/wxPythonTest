#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# @Time    : 2018-12-22
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : wxPython编程学习笔记(04)wx.Butoon的应用
# @Url     : http://www.17python.com/blog/90
# @Details : wxPython编程学习笔记(04)wx.Butoon的应用
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm



'''

## wx.Butoon

按钮是在GUI中使用率最高的一种组件了，点击按钮触发事件可以说是非常普遍的事了。`wx.Button`使用起来操作简单。
wx中开关按钮`ToggleButton`，类似于电灯开关，绑定事件后可以通过

    obj = e.GetEventObject()
    isPressed = obj.GetValue()

来获取对象的属性，这样就可以知道开关按钮的状态了。


## Button的创建与使用

创建

    bt = wx.Button(self,label="关闭窗口",)

绑定事件

    bt.Bind(wx.EVT_BUTTON, self.onCloseWindow)

然后编写绑定事件的函数方法，这样就可以调用此方法了。


具体代码如下，希望这些短小的代码，能给您带来帮助。




'''

import wx

class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        #调用父类的创建方法
        super(HelloFrame, self).__init__(*args, **kw)

        box = wx.BoxSizer(wx.VERTICAL)
        bt1 = wx.Button(self,label="关闭窗口",)
        bt1.Bind(wx.EVT_BUTTON, self.onCloseWindow)


        self.bt2 = wx.ToggleButton(self,label='开关')
        self.bt2.Bind(wx.EVT_TOGGLEBUTTON,self.showFlash)
        st = wx.TextCtrl(self,value='helloworld',)


        box.AddMany([(bt1,0, wx.ALL | wx.EXPAND, 0),(self.bt2,0, wx.ALL | wx.EXPAND, 0),(st,0, wx.ALL | wx.EXPAND | wx.SHAPED, 0)])


        self.SetSizer(box)


    def onCloseWindow(self,e):
        dl = wx.MessageDialog(None,"是否要关闭窗口？","请选择",wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        ret = dl.ShowModal()

        if ret == wx.ID_YES:
            self.Destroy()
        else:
            pass

    def showFlash(self,e):
        obj = e.GetEventObject()
        isPressed = obj.GetValue()

        if isPressed:
            self.bt2.SetLabel("关闭")
        else:
            self.bt2.SetLabel("打开")


def main():
    app = wx.App()
    frm = HelloFrame(None, title='wxPython Button',)
    frm.Show()#显示窗口
    app.MainLoop()#持续更新窗口


if __name__ == '__main__':
        main()