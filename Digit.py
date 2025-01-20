import wx

class Digit(wx.StaticText):

  def __init__(self, parent, label = '0', size = 20):
    super().__init__(parent, label = label)
    self.SetFont(wx.Font(size, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
    
  def update(self, label):
    self.SetLabel(label)
