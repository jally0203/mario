import wx

def onClick(evt):
  print('hi')

app = wx.App()
frame = wx.Frame(None)
panel = wx.Panel(frame)

btn = wx.Button(panel, label = "OK")

btn.Bind(wx.EVT_KEY_DOWN, onClick)

frame.Show()
app.MainLoop()


