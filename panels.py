#! usr/bin/env python

import wx

class windowClass(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(windowClass, self).__init__(*args, **kwargs)

		self.basicGUI()

	def basicGUI(self):

		panel = wx.Panel(self) # Create text box
		menuBar = wx.MenuBar() # Create menu bar
		fileButton = wx.Menu() # creates single menu - e.g., File button
		editButton = wx.Menu()
		exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'Status: Exiting window...')
		menuBar.Append(fileButton, 'File') # Append buttons to menu
		menuBar.Append(editButton, 'Edit')
		wx.TextCtrl(panel, pos = (10,10), size=(500,500), style = wx.TE_MULTILINE) # create text box
		self.SetMenuBar(menuBar)
		self.Bind(wx.EVT_MENU, self.Quit, exitItem)
		self.Maximize()
		self.Show()

	def Quit(self, event):
		self.Close()


def main():
	app = wx.App()
	windowClass(None, title = 'Mein Window')
	app.MainLoop()

if __name__ == '__main__':
	main()


