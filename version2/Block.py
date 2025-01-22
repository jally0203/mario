import wx

class Block(wx.Panel):

  def __init__(self, parent, size = (50, 50), color = wx.BLACK, pos = (0, 0)):
    super().__init__(parent)
    self.SetSize(size)
    self.SetBackgroundColour(color)
    self.SetPosition(pos)
    
