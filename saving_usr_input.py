#! usr/bin/env python

import wx

class windowClass(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(windowClass, self).__init__(*args, **kwargs)

		self.basicGUI()

	def basicGUI(self):

		#MENUBAR
		menuBar = wx.MenuBar()
		fileButton = wx.Menu()
		editButton = wx.Menu()
		exitItem = fileButton.Append(wx.ID_EXIT, 'Quit', 'Status: Closing window...')
		menuBar.Append(fileButton, 'File')
		menuBar.Append(editButton, 'Edit')
		self.Bind(wx.EVT_MENU, self.Quit, exitItem)
		self.SetMenuBar(menuBar)
		# PANEL
		panel = wx.Panel(self) 
		write = wx.TextCtrl(panel, pos= (50,50), size = (300,300), style = wx.TE_MULTILINE)
		# DIALOGUES
		nameBox = wx.TextEntryDialog(None, 'What is your name?', 'Welcome', 'name')
		yesNoBox = wx.MessageDialog(None, 'Do you enjoy wxPython?', 'Question', wx.YES_NO)
		yesNoAnswer = yesNoBox.ShowModal()
		yesNoBox.Destroy()

		if nameBox.ShowModal() == wx.ID_OK:
			userName = nameBox.GetValue()
		if yesNoAnswer == wx.ID_NO:
			userName = 'Loser'
			write.AppendText('Losers do not enjoy wxPython!')
		# SHOW
		self.SetTitle('Welcome '+userName)
		self.Show()

	def Quit(self, event):
		self.Close()


def main():
	app = wx.App()
	windowClass(None, title = "New Window")
	app.MainLoop()

if __name__ == '__main__':
	main()