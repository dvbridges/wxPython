#!usr/binenv python
import wx

text_1 = "Hello back! Welcome to the standard text input"

app = wx.App()
frame = wx.Frame(None, -1, "Hello World", size = (400,400),pos = (500,200))
	#style =  wx.CLOSE_BOX | wx.CAPTION | wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX)
panel = wx.Panel(frame)
label = wx.StaticText(panel, label = text_1, pos = (150,150), size = (100,100))
frame.Show(True)
app.MainLoop()