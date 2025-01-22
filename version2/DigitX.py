import wx

from Block import Block

class DigitX(wx.Window):

  def __init__(self, parent, pos = (0, 0), size = (80, 50)):
    super().__init__(parent)    
    self.size = size
    self.num = 0   
    #self.timer = wx.Timer(self)        
    self.coor = [(10, 40), (10, 10), \
                 (40, 40), (40, 10), \
                 (70, 40), (70, 10) ]
    self.SetBackgroundColour(wx.BLACK)
    self.SetPosition(pos)
    self.SetSize(size)             
    self.Bind(wx.EVT_PAINT, self.onPaint)
    #self.Bind(wx.EVT_TIMER, self.onTimer)
    #self.timer.Start(1000)
    
  def onTimer(self, evt):
    self.num += 1
    if self.num == 10:
      self.num = 0
    self.Refresh()
    
  def setNum(self, num):
    self.num = num
    self.Refresh()
    
  def update(self, n):
    self.num = n
    self.Refresh()
    
  def onPaint(self, evt):  
    dc = wx.PaintDC(self)
    dc.Clear()
    dc.SetPen(wx.Pen(wx.YELLOW, 2))
    n = self.num
    print(n)
    if n != 1 and n != 4:  # 2 3 5 6 7 8 9 0
      print('1', n)
      dc.DrawLine(self.coor[0][0], self.coor[0][1], self.coor[1][0], self.coor[1][1])
    if n != 1 and n != 2 and n != 3 and n != 7:  # 4 5 6 8 9 0  
      print('2', n)
      dc.DrawLine(self.coor[0][0], self.coor[0][1], self.coor[2][0], self.coor[2][1])
    if n != 5 and n != 6: # 1 2 3 4 7 8 9 0  
      print('3', n)
      dc.DrawLine(self.coor[1][0], self.coor[1][1], self.coor[3][0], self.coor[3][1])
    if n != 1 and n != 7 and n != 0: # 2 3 4 5 6 8 9 
      print('4', n)
      dc.DrawLine(self.coor[2][0], self.coor[2][1], self.coor[3][0], self.coor[3][1])
    if n == 2 or n == 6 or n == 8 or n == 0: # 2 6 8 0
      print('5', n)
      dc.DrawLine(self.coor[2][0], self.coor[2][1], self.coor[4][0], self.coor[4][1])
    if n != 2 : # 1 3 4 5 6 7 8 9 0
      print('6', n)
      dc.DrawLine(self.coor[3][0], self.coor[3][1], self.coor[5][0], self.coor[5][1])
    if n != 1 and n != 4 and n != 7: # 2 3 5 6 8 9 0
      print('7', n)
      dc.DrawLine(self.coor[4][0], self.coor[4][1], self.coor[5][0], self.coor[5][1])
    
    
