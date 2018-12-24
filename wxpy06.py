#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# @Time    : 2018-12-23
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : wxPython编程学习笔记(06)wx.ComboBox下拉列表框
# @Url     : http://www.17python.com/blog/92
# @Details : wxPython编程学习笔记(06)wx.ComboBox下拉列表框
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm



'''

## wx.ComboBox下拉列表框

下拉列表框，可以通过下拉列表选择内容，在使用中可以为内容节省不少空间，是GUI中比较常用的小部件。

## wx.ComboBox的创建与绑定


        #创建ComboBox
        l = ["Python","Django","Flask","wxPython","Java"]
        cb = wx.ComboBox(pnl, pos=(20, 20), choices=l,style=wx.CB_READONLY)
        cb.Bind(wx.EVT_COMBOBOX, self.OnSelect)

通过以上方法即可简单的创建`ComboBox`与绑定事件.

具体代码再下边，跑下即可了解。





'''

import wx

class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        #调用父类的创建方法
        super(HelloFrame, self).__init__(*args, **kw)
        pnl = wx.Panel(self)
        hbox = wx.BoxSizer(wx.VERTICAL)

        #创建ComboBox
        l = ["Python","Django","Flask","wxPython","Java"]
        cb = wx.ComboBox(pnl, pos=(20, 20), choices=l,style=wx.CB_READONLY)
        cb.Bind(wx.EVT_COMBOBOX, self.OnSelect)
        hbox.Add(cb,0,wx.CENTER|wx.EXPAND,20)

        #创建一个静态文本用来显示上拉列表框选择的内容
        self.st = wx.StaticText(pnl, label='请点选ComboBox')
        hbox.Add(self.st,0,wx.CENTER|wx.TOP,20)


        pnl.SetSizer(hbox)

    def OnSelect(self,e):
        s = e.GetString()
        self.st.SetLabel(s)


def main():
    app = wx.App()
    frm = HelloFrame(None, title='wxPython Button',)
    frm.Show()#显示窗口
    app.MainLoop()#持续更新窗口


if __name__ == '__main__':
        main()