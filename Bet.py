import wx

class Bet(wx.BitmapButton):
  
  def __init__(self, parent, imgFile, award, key):
    self.bitmap = wx.Bitmap(imgFile, wx.BITMAP_TYPE_ANY)
    super().__init__(parent, bitmap=self.bitmap)
    self.award = award
    self.myBet = 0
    self.myDigit = None
    self.keyAscii = ord(key)
    self.enableFlag = True
    self.Bind(wx.EVT_BUTTON, self.onClick)
    self.Refresh()
        
  def onClick(self, evt):
    if self.enableFlag:
      self.addBet()
      
  def patch(self, evt):
    if evt.GetKeyCode() == self.keyAscii:      
      self.onClick(None)
    
  def getBet(self):
    return self.myBet
    
  def getAward(self):
    return self.award
    
  def addBet(self):
    if self.myBet < 99:
      self.myBet += 1
      if self.myBet >= 10:
        self.betStr = str(self.myBet)
        self.myDigitH.update(int(self.betStr[0]))
        self.myDigitL.update(int(self.betStr[1]))
      else:
        self.betStr = str(self.myBet)
        self.myDigitH.update(0)
        self.myDigitL.update(int(self.betStr[0]))
        
  def clearBet(self):
    self.myBet = 0
    self.myDigit.update(str(self.myBet))
    
  def enableClick(self, onoff):
    self.enableFlag = onoff
    
  def setDigitL(self, digit):
    self.myDigitL = digit
    
  def setDigitH(self, digit):
    self.myDigitH = digit

