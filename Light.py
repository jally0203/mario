import wx

class Light(wx.StaticBitmap):

  def __init__(self, parent, bitmap_on, bitmap_off, pos, size = (55, 58)):
    super().__init__(parent, -1, bitmap = bitmap_off)
    self.bitmap_on = bitmap_on
    self.bitmap_off = bitmap_off
    self.SetPosition(pos)
    self.SetSize(size)
    self.award = 0
    self.fruit = 0

  def set(self):
    self.SetBitmap(self.bitmap_on)
  
  def clear(self):
    self.SetBitmap(self.bitmap_off)
    
  def setPair(self, award, fruit):
    self.award = award
    self.fruit = fruit
    
  def getPair(self):  
    return self.award, self.fruit
      
