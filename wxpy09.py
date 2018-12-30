#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# @Time    : 2018-12-27
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : wxPython编程学习笔记(06)wx.ListBox 下拉列表框
# @Url     : http://www.17python.com/blog/94
# @Details : wxPython编程学习笔记(06)wx.ListBox 下拉列表框
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm



'''

## wx.ListBox 下拉列表框






'''

import os
import wx

DATAFILE = os.path.join(os.path.dirname(__file__), '17python')



class MyPopupMenu(wx.Menu):

    def __init__(self, parent):
        super(MyPopupMenu, self).__init__()

        self.parent = parent

        mmi = wx.MenuItem(self, wx.NewId(), 'Minimize')
        self.Append(mmi)
        self.Bind(wx.EVT_MENU, self.OnMinimize, mmi)

        cmi = wx.MenuItem(self, wx.NewId(), 'Close')
        self.Append(cmi)
        self.Bind(wx.EVT_MENU, self.OnClose, cmi)


    def OnMinimize(self, e):
        self.parent.Iconize()

    def OnClose(self, e):
        self.parent.Close()

class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        #调用父类的创建方法
        super(HelloFrame, self).__init__(*args, **kw)

        self.menubar = wx.MenuBar()
        self.fileMenu = wx.Menu()

        self.new = wx.MenuItem(self.fileMenu,9,"new")
        self.fileMenu.Append(self.new)

        self.editMenu = wx.Menu()
        self.copyItem = wx.MenuItem(self.editMenu, 100, text="copy", kind=wx.ITEM_NORMAL)
        self.editMenu.Append(self.copyItem)
        self.cutItem = wx.MenuItem(self.editMenu, 101, text="cut", kind=wx.ITEM_NORMAL)
        self.editMenu.Append(self.cutItem)
        self.pasteItem = wx.MenuItem(self.editMenu, 102, text="paste", kind=wx.ITEM_NORMAL)
        self.editMenu.Append(self.pasteItem)

        self.fileMenu.Append(22, "Edit", self.editMenu)
        self.fileMenu.AppendSeparator()
        self.fileMenu.AppendSeparator()#分隔线
        self.qmi = wx.MenuItem(self.fileMenu, 1, '&Quit\tCtrl+Q')
        self.fileMenu.Append(self.qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, id=1)

        self.menubar.Append(self.fileMenu, '&File')
        self.SetMenuBar(self.menubar)

        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

    def OnRightDown(self, e):
        self.PopupMenu(MyPopupMenu(self), e.GetPosition())

    def OnQuit(self, e):
        self.Close()

def main():
    app = wx.App(False)
    frm = HelloFrame(None, title='wx.MenuBar 菜单',)
    frm.Show()#显示窗口
    app.MainLoop()#持续更新窗口


if __name__ == '__main__':
        main()