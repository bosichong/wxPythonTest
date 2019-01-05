#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @Time    : 2019-01-05
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : wxPython编程学习笔记(10)wx.FileDialog文件选择框
# @Url     : http://www.17python.com/blog/95
# @Details : wxPython编程学习笔记(10)wx.FileDialog文件选择框
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm




'''
## wx.FileDialog文件选择框

'FileDialog'是一个文件选择框，我们可以根据弹出框选择文件，确定后返回该文件的地址。


## 创建


    dlg = wx.FileDialog(parent, message=None, defaultDir=None, defaultFile=None, wildcard=None, style=None, pos=None, size=None, name=None)
    dlg.GetPath()#返回文件地址字符串
    
    
其打开方式和其它弹出窗口一样有模态和非模态，当按下确认按钮后，返回一个文件地址字符串。

我做了一个测试，代码下边跑跑看吧，希望能帮助到你。
'''


import wx
import os
import time

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):

        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_1 = wx.Button(self, wx.ID_ANY, u"选择文件")
        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, "")

        self.__set_properties()
        self.__do_layout()


    def __set_properties(self):

        self.SetTitle("frame")
        self.button_1.Bind(wx.EVT_BUTTON,self.onButton_1)

    def __do_layout(self):

        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.text_ctrl_1, 1, wx.ALL, 0)
        sizer_2.Add(self.button_1, 0, 0, 0)
        sizer_1.Add(sizer_2, 0, wx.ALL | wx.EXPAND, 0)
        sizer_3.Add(self.text_ctrl_2, 1, wx.ALL | wx.EXPAND, 0)
        sizer_1.Add(sizer_3, 1, wx.ALL | wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()

    def onButton_1(self,e):
        print("按钮事件")
        dlg = wx.FileDialog(self, message="选择一个文件", defaultDir=os.getcwd(), style=wx.FD_OPEN)
        ret = dlg.ShowModal()
        if ret == wx.ID_OK:
            print(dlg.GetPath())  # 文件地址
            self.text_ctrl_1.SetValue(dlg.GetPath())

            fp = os.path.join(dlg.GetPath())  # 组装文件地址
            ###输出到弹出信息窗口的字符拼装。
            retstr = str(self.get_FileSize(fp)) + "\n" + self.get_FileAccessTime(fp) + "\n" + self.get_FileCreateTime(
                fp) + "\n" + self.get_FileModifyTime(fp)
            self.text_ctrl_2.SetValue(retstr)

        dlg.Destroy()


    # 把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12
    def TimeStampToTime(self, timestamp):
        timeStruct = time.localtime(timestamp)
        return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)

    # 获取文件的大小,结果保留两位小数，单位为MB
    def get_FileSize(self, filePath):
        fsize = os.path.getsize(filePath)
        return fsize

    # 获取文件的访问时间
    def get_FileAccessTime(self, filePath):
        t = os.path.getatime(filePath)
        return self.TimeStampToTime(t)

    # 获取文件的创建时间
    def get_FileCreateTime(self, ilePath):
        t = os.path.getctime(ilePath)
        return self.TimeStampToTime(t)

    # 获取文件的修改时间
    def get_FileModifyTime(self, filePath):
        t = os.path.getmtime(filePath)
        return self.TimeStampToTime(t)
class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
