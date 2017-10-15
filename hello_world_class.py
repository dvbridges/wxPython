#!usr/binenv python
import wx

class windowClass(wx.Frame):

	def __init__(self, parent, title):
		super(windowClass, self).__init__(parent, title = title, size = (800,600))

		self.Show()
		# self.Move((350, 100))
		self.Centre()

app = wx.App()
windowClass(None, title = "Window Class")
app.MainLoop()