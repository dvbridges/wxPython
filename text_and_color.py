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
		saveItem = fileButton.Append(wx.ID_SAVE, 'Save', 'Saving text to .csv')
		menuBar.Append(fileButton, 'File')
		menuBar.Append(editButton, 'Edit')
		self.Bind(wx.EVT_MENU, self.Quit, exitItem)
		self.Bind(wx.EVT_MENU, self.Save, saveItem)
		self.SetMenuBar(menuBar)
		# PANEL
		panel = wx.Panel(self) 
		self.write = wx.TextCtrl(panel, pos= (50,50), size = (300,300), style = wx.TE_MULTILINE)
		aweText = wx.StaticText(panel, -1, "Awesome Text", (50,10))
		aweText.SetForegroundColour('steelblue')
		aweText.SetBackgroundColour('lightyellow')
		# DIALOGUES
		nameBox = wx.TextEntryDialog(None, 'What is your name?', 'Welcome', '')
		yesNoBox = wx.MessageDialog(None, 'Do you enjoy wxPython?', 'Question', wx.YES_NO)
		yesNoAnswer = yesNoBox.ShowModal()
		yesNoBox.Destroy()

		if nameBox.ShowModal() == wx.ID_OK:
			userName = nameBox.GetValue()
		if yesNoAnswer == wx.ID_NO:
			userName = 'Loser'
			self.write.AppendText('Losers do not enjoy wxPython! ')

		choice = wx.SingleChoiceDialog(None, 'Please choose your operating system:',
			'Operating system',('Windows','Linux'))
		if choice.ShowModal() == wx.ID_OK:
			OS_selection = choice.GetStringSelection() 
			self.write.AppendText('You chose to use {}.'.format(OS_selection))
			choice.Destroy()

		col_choice = wx.SingleChoiceDialog(None, 'Please choose your favourite color',
			'Color choice',('Red','Blue','Green'))
		if col_choice.ShowModal() == wx.ID_OK:
			col_selection = col_choice.GetStringSelection() 
			aweText.SetForegroundColour(col_selection)
			col_choice.Destroy()


		# SHOW
		self.SetTitle('Welcome '+userName)
		self.Show()

	def Quit(self, event):
		self.Close()

	def Save(self, event):
		f = open('some.csv', 'w')
		f.write(self.write.GetValue())
		f.close()

def main():
	app = wx.App()
	windowClass(None, title = "New Window")
	app.MainLoop()

if __name__ == '__main__':
	main()