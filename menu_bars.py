#! usr/bin/env python

import wx

class windowClass(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(windowClass, self).__init__(*args, **kwargs)

		self.basicGUI()

	def basicGUI(self):
		menuBar = wx.MenuBar()
		fileButton = wx.Menu()
		exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'Status: Exiting window...')
		menuBar.Append(fileButton, 'File')

		self.SetMenuBar(menuBar)
		self.Bind(wx.EVT_MENU, self.Quit, exitItem)
		self.SetTitle('New Window')
		self.Maximize(True)
		self.Show(True)

	def Quit(self, e):
		self.Close()

def main():
	app = wx.App()
	windowClass(None, title = "Window Frame")
	app.MainLoop()
	wx.Frame()

if __name__ == '__main__':
	main()

