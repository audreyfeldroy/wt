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

        # Top controls
        topPanel = wx.Panel(self)
        self.usernameList = ['audrey71', 'danny04', 'cartwheel51']
        comboBox = wx.ComboBox(self, choices=self.usernameList, style=wx.CB_DROPDOWN)

        # Main usable area
        mainpanel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(wx.StaticText(panel, label="Some tweet"))

        self.Show()


app = wx.App(False)
TweetFrame(None)
app.MainLoop()

