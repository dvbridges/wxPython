#! usr/bin/env python

# define class
# set gui function
# create panel
# create menuBar
# ccreate buttons/menus
# append items to buttons/menus
# append menus to menubar
# set text panel
# bind functions or events to menu items
# set menu bar
# maximize and show
# Define quit box
# main()

import wx

class windowClass(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(windowClass, self).__init__(*args, **kwargs)

		self.basicGUI()

	def basicGUI(self):
		panel = wx.Panel(self)
		menuBar = wx.MenuBar()
		fileButton = wx.Menu()
		editButton = wx.Menu()
		exitItem = fileButton.Append(wx.ID_EXIT, 'Quit', 'Status: Closing window...')
		menuBar.Append(fileButton, 'File')
		menuBar.Append(editButton, 'Edit')
		wx.TextCtrl(panel, pos= (50,50), size = (300,300), style = wx.TE_MULTILINE)
		self.Bind(wx.EVT_MENU, self.Quit, exitItem)
		self.SetMenuBar(menuBar)
		self.Maximize()
		self.Show()

	def Quit(self, event):
		self.Close()


def main():
	app = wx.App()
	windowClass(None, title = "New Window")
	app.MainLoop()

if __name__ == '__main__':
	main()