#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx

class TweetFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="WT Beta")
        menuBar = wx.MenuBar()
        menu = wx.Menu()
        m_exit = menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Close window and exit program.")
        menuBar.Append(menu, "&File")
        self.SetMenuBar(menuBar)

        # BoxSizer holds all controls below menu
        box = wx.BoxSizer(wx.VERTICAL)

        # Username dropdown
        self.usernameList = ['audrey71', 'danny04', 'cartwheel51']
        comboBox = wx.ComboBox(self, choices=self.usernameList, style=wx.CB_DROPDOWN)
        box.Add(comboBox, flag=wx.EXPAND)

        # Tweets static control
        tweets = wx.StaticText(self, label="Some tweet asfdas sadfj kasdj fldksj sdklf jlskd lskdf skld fsdklf jsdklj dslf jsdl skldfjasdkljf lskdj flksdjf lkdjf ksdj ksdjf sdkjkl ds.")
        box.Add(tweets, flag=wx.EXPAND)

        # Set the BoxSizer and show the frame
        self.SetSizer(box)
        self.Show()


app = wx.App(False)
TweetFrame(None)
app.MainLoop()

