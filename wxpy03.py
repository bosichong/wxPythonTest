#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# @Time    : 2018-12-21
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : wxPython编程学习笔记(03)wxPython中的事件
# @Url     : http://www.17python.com/blog/89
# @Details : wxPython编程学习笔记(03)wxPython中的事件
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm



'''

## wxPython中的事件

和大多数GUI程序一样，wxPython也有许多的事件可以绑定，这样才会有点击按钮发生行为事件的可能。

wxPython中的事件绑定很简单：

    self.Bind(wx.EVT_MOVE,self.onMove)

上边一行代码就完成了一个事件的绑定，当窗口移动时的事件，`self.onMove`就是这个事件处发时要执行的方法函数。
我们只要在`class`中定义`self.onMove`方法的代码，然后当事件触发时，就可以执行`onMove`方法了。

`wx.EVT_XXXXX`这种类似的常量定义大量的事件，我们可以通过官方的文档进行查询，根据自己的需求选择所要发生的事件。

好了，wxPython中的事件处理是不是很简单？至少我认为比Tk中的事件绑定更直观简单一些。





'''

import wx

class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        #调用父类的创建方法
        super(HelloFrame, self).__init__(*args, **kw)


        #创建一组文本用来显示数值
        wx.StaticText(self,label="x:",pos=(10,10))
        wx.StaticText(self, label="y:", pos=(10, 30))

        self.st1 = wx.StaticText(self, label='', pos=(30, 10))
        self.st2 = wx.StaticText(self, label='', pos=(30, 30))
        #绑定窗口移动事件
        self.Bind(wx.EVT_MOVE,self.onMove)
        #绑定窗口关闭事件
        self.Bind(wx.EVT_CLOSE,self.onCloseWindow)

    def onMove(self,e):
        x,y = e.GetPosition()
        self.st1.SetLabel(str(x))
        self.st2.SetLabel(str(y))

    def onCloseWindow(self,e):
        dl = wx.MessageDialog(None,"是否要关闭窗口？","请选择",wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        ret = dl.ShowModal()

        if ret == wx.ID_YES:
            self.Destroy()
        else:
            pass


def main():
    app = wx.App()
    frm = HelloFrame(None, title='Events in wxPython',pos=(300,300))
    frm.Show()#显示窗口
    app.MainLoop()#持续更新窗口


if __name__ == '__main__':
        main()