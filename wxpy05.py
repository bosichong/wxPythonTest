#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# @Time    : 2018-12-23
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : wxPython编程学习笔记(05)单选及多选按钮
# @Url     : http://www.17python.com/blog/91
# @Details : wxPython编程学习笔记(05)单选及多选按钮
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm



'''

## wxPython单选及多选按钮

单选及多选按钮也是程序中经常使用到的互动小部件，使用频率也是很高的，对于选择按钮，我们重点需要了解的就是触发事件，
通常，单选我们需要得到一组按钮中的选择项值或是键值，多选，我们只要知道每一项返回的布尔值即可。

##多选按钮wx.CheckBox

创建及绑定事件

    cb1=wx.CheckBox(pnl, label='hello', )
    self.Bind(wx.EVT_CHECKBOX,self.onCheckBox)

这里的`self.Bind`是指绑定了当前窗口中所有的多选按钮，如果需要单独绑定，则需要为每一个多选按钮做单独的事件绑定。

## 单选按钮组wx.RadioBox

这里我直接介绍`wx.RadioBox`，因为单选按钮基本上是一组呈现的，所以直接使用单选按钮组即可，还方便。

创建及绑定

    self.radio_box_1 = wx.RadioBox(pnl, wx.ID_ANY, u"请选择", choices=["aaa", "bbb", "ccccc", "ddddd"], majorDimension=1,
                                  style=wx.RA_SPECIFY_ROWS)
    self.radio_box_1.Bind(wx.EVT_RADIOBOX,self.onRadiobox)

代码很直观，`majorDimension`表示单选钮的排列方式：0横向，1竖向。

好了，完整的代码在下边，可以跑跑看。






'''

import wx

class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        #调用父类的创建方法
        super(HelloFrame, self).__init__(*args, **kw)
        pnl = wx.Panel(self)


        hbox3 = wx.StaticBoxSizer(wx.StaticBox(pnl, label='多选及单选测试',), wx.VERTICAL)
        cb1=wx.CheckBox(pnl, label='hello', )
        cb2=wx.CheckBox(pnl, label='world', )
        self.Bind(wx.EVT_CHECKBOX,self.onCheckBox)
        self.radio_box_1 = wx.RadioBox(pnl, wx.ID_ANY, u"请选择", choices=["aaa", "bbb", "ccccc", "ddddd"], majorDimension=1,
                                  style=wx.RA_SPECIFY_ROWS)
        self.radio_box_1.Bind(wx.EVT_RADIOBOX,self.onRadiobox)

        hbox3.AddMany([(cb1),(cb2),(self.radio_box_1, 0, wx.EXPAND|wx.TOP, 10)])

        btn = wx.Button(pnl, label='Ok', pos=(90, 185), size=(60, -1))

        btn.Bind(wx.EVT_BUTTON, self.OnClose)

        pnl.SetSizer(hbox3)


    def onRadiobox(self,e):
        rb = e.GetEventObject()
        print(rb.GetSelection(),rb.GetStringSelection())#打印当前单选按钮的选项

    def onCheckBox(self,e):
        cb = e.GetEventObject()
        if cb.GetValue():
            print(cb.GetLabel())

    def OnClose(self, e):
        self.Close(True)




def main():
    app = wx.App()
    frm = HelloFrame(None, title='wxPython Button',)
    frm.Show()#显示窗口
    app.MainLoop()#持续更新窗口


if __name__ == '__main__':
        main()