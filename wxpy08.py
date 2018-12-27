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

wx.ListBox是以中数据展示的小部件，使用方便简单，可以用来展示比较单一的数据，例如：各种地址，名称列表等。
这次准备了一个基于wx.ListBox构建的小小通讯录，实现了增删改但是木有查，为什么没有查？因为我没写，就这样了。
具体效果展示如下：


## wx.ListBox的创建及一些方法

创建

    listbox = wx.ListBox(panel,choices=ls)

ListBox 有些常用的方法，用来处理列表中的数据

    listbox.Append(text) 添加
    listbox.GetSelection() 获取索引
    listbox.GetString(sel) 通过索引获取字符串
    listbox.Delete(sel) 删除当前索引
    listbox.Insert(renamed, sel) 在当前索引处添加新的值，返回当前索引
    listbox.SetSelection(item_id) 根据索引值选择项
    listbox.Clear() 清空当前列表

## 通讯录的数据保存

作为一个简单的通讯录应该能保存数据，处于简单化处理，我只保存一个文本到目录下，若是需要可以使用数据库。
通讯录在操作的同时我们要更新保存数据，所以，我建了三个方法，分别处理新建数据文本，打开读取，保存数据。
分别对应：newFile openFile saveFile,这样配合这几个方法就可以实现一个简单的通讯录了。

具体代码如下，可以跑跑看啦：




'''

import os
import wx

DATAFILE = os.path.join(os.path.dirname(__file__), '17python')

class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        #调用父类的创建方法
        super(HelloFrame, self).__init__(*args, **kw)
        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.newFile()
        ls = self.openFile()
        self.listbox = wx.ListBox(panel,choices=ls)
        hbox.Add(self.listbox, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)

        btnPanel = wx.Panel(panel)
        vbox = wx.BoxSizer(wx.VERTICAL)
        newBtn = wx.Button(btnPanel, wx.ID_ANY, '新建', size=(90, 30))
        renBtn = wx.Button(btnPanel, wx.ID_ANY, '修改', size=(90, 30))
        delBtn = wx.Button(btnPanel, wx.ID_ANY, '删除', size=(90, 30))
        clrBtn = wx.Button(btnPanel, wx.ID_ANY, '清空', size=(90, 30))

        self.Bind(wx.EVT_BUTTON, self.NewItem, id=newBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnRename, id=renBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnDelete, id=delBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnClear, id=clrBtn.GetId())
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.OnRename)

        vbox.Add((-1, 20))
        vbox.Add(newBtn)
        vbox.Add(renBtn, 0, wx.TOP, 5)
        vbox.Add(delBtn, 0, wx.TOP, 5)
        vbox.Add(clrBtn, 0, wx.TOP, 5)

        btnPanel.SetSizer(vbox)
        hbox.Add(btnPanel, 0.6, wx.EXPAND | wx.RIGHT, 20)
        panel.SetSizer(hbox)

        self.SetTitle('wx.ListBox')
        self.Centre()



    def NewItem(self, event):

        text = wx.GetTextFromUser('Enter a new item', 'Insert dialog')
        if text != '':
            self.listbox.Append(text)
        self.saveFile()

    def OnRename(self, event):

        sel = self.listbox.GetSelection()
        text = self.listbox.GetString(sel)
        renamed = wx.GetTextFromUser('Rename item', 'Rename dialog', text)

        if renamed != '':
            self.listbox.Delete(sel)
            item_id = self.listbox.Insert(renamed, sel)
            self.listbox.SetSelection(item_id)

        self.saveFile()

    def OnDelete(self, event):

        sel = self.listbox.GetSelection()
        if sel != -1:
            self.listbox.Delete(sel)

        self.saveFile()

    def OnClear(self, event):
        self.listbox.Clear()
        self.saveFile()


    def newFile(self):
        if not os.path.isfile(os.path.join(DATAFILE)):
            with open(os.path.join(DATAFILE), mode='a+', encoding='utf-8') as f:
                pass

    def saveFile(self):
        '''保存数据'''
        s = self.listbox.Items
        with open(os.path.join(DATAFILE),mode='w+',encoding='utf-8') as f:
            f.write(str(s))



    def openFile(self):
        '''读取文件'''
        with open(os.path.join(DATAFILE),mode='r+',encoding='utf-8') as f:
            s = f.read()
            print(s)
            if s == "":
                s = "['请添加通讯数据']"
                return eval(s)
            return eval(s)

def main():
    app = wx.App()
    frm = HelloFrame(None, title='wx.ListBox 通讯录',)
    frm.Show()#显示窗口
    app.MainLoop()#持续更新窗口


if __name__ == '__main__':
        main()