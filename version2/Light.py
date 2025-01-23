import wx

class Light(wx.StaticBitmap):

  def __init__(self, parent, bitmap_on, bitmap_off, pos, size = (55, 58)):
    super().__init__(parent, -1, bitmap = bitmap_off)
    self.bitmap_on = bitmap_on
    self.bitmap_off = bitmap_off
    self.SetPosition(pos)
    self.SetSize(size)
    self.award = 0
    self.type = 0

  def set(self):0
    self.SetBitmap(self.bitmap_on)
  
  def clear(self):
    self.SetBitmap(self.bitmap_off)
        
  def setAward(self, award):
    self.award = award
    
  def getAward(self):
    return self.award
    
  def setType(self, type):
    self.type = type
    
  def getType(self):
    return self.type

