import wx

from DigitX import DigitX

class FourDigits(wx.Panel):
  
  def __init__(self, parent, pos, size):
    super().__init__(parent)    
    self.num = 0
    self.digits = []
    for i in range(3, -1, -1):
      self.digits.append(DigitX(self, (0, i * 50)))
    self.SetPosition(pos)
    self.SetSize(size)
    self.update()
    
  def setNum(self, n):
    self.num = n
    self.update()
    
  def getNum(self):
    return self.num
    
  def update(self):
    vs = str(self.num)
    zvs = vs.zfill(4)   # zero padding
    for i in range(4):
      self.digits[i].update(int(zvs[i]))     
      
class Credit(FourDigits):

  def __init__(self, parent, pos, size = (80, 200)):
    super().__init__(parent, pos, size)
    #self.setNum(0)
    
class Win(FourDigits):
 
  def __init__(self, parent, pos, size = (80, 200)):
    super().__init__(parent, pos, size)
    self.setNum(0)
