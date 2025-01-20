import wx

from Block import Block

class Digit3(wx.Window):

  def __init__(self, parent, pos = (0, 0), size = (80, 50)):
    super().__init__(parent)    
    self.size = size
    self.num = 0   
    self.timer = wx.Timer(self)        
    self.timer.Start(1000)
    self.coor = [(10, 40), (10, 10), \
                 (40, 40), (40, 10), \
                 (70, 40), (70, 10) ]
    self.SetBackgroundColour(wx.BLACK)
    self.SetPosition(pos)
    self.SetSize(size)             
    self.Bind(wx.EVT_PAINT, self.onPaint)
    self.Bind(wx.EVT_TIMER, self.onTimer)
    
  def onTimer(self, evt):
    self.num += 1
    if self.num == 10:
      self.num = 0
    self.dc = wx.PaintDC(self)
    self.dc.Clear()
    self.dc.SetPen(wx.Pen(wx.YELLOW, 2))    
    self.draw(self.num)
    
  def setNum(self, num):
    self.num = num
    
  def update(self, n):
    self.num = n
    self.Refresh()
    
  def onPaint(self, evt):  
    print('onPaint')
    #self.dc = wx.PaintDC(self)
    #self.dc.Clear()
    #self.dc.SetPen(wx.Pen(wx.YELLOW, 2))
    #self.dc.DrawLine(100, 100, 200, 200)
    #self.draw(self.num)
    
  def draw(self, n):
    if n != 1 and n != 4:  # 2 3 5 6 7 8 9 0
      self.seg1()
    if n != 1 and n != 2 and n != 3 and n != 7:  # 4 5 6 8 9 0  
      self.seg2()
    if n != 5 and n != 6: # 1 2 3 4 7 8 9 0  
      self.seg3()
    if n != 1 and n != 7 and n != 0: # 2 3 4 5 6 8 9 
      self.seg4()  
    if n == 2 or n == 6 or n == 8 or n == 0: # 2 6 8 0
      self.seg5()  
    if n != 2 : # 1 3 4 5 6 7 8 9 0
      self.seg6()  
    if n != 1 and n != 4 and n != 7: # 2 3 5 6 8 9 0
      self.seg7()  
    
  def draw0(self):
    self.seg1()  
    self.seg2()
    self.seg3()
    self.seg5()
    self.seg6()
    self.seg7()
    
  def draw1(self):    
    self.seg2()
    self.seg5()
  
  def draw2(self):
    self.seg1()  
    self.seg3()
    self.seg4()
    self.seg5()    
    self.seg7()
  
  def draw3(self):
    self.seg1()      
    self.seg3()
    self.seg4()    
    self.seg6()
    self.seg7()
  
  def draw4(self):    
    self.seg2()
    self.seg3()
    self.seg4()    
    self.seg6()
  
  def draw5(self):
    self.seg1()  
    self.seg2()
    self.seg4()
    self.seg6()
    self.seg7()
  
  def draw6(self):
    self.seg1()  
    self.seg2()
    self.seg4()
    self.seg5()
    self.seg6()
    self.seg7()
  
  def draw7(self):
    self.seg1()  
    self.seg2()
    self.seg3()    
    self.seg6()
  
  def draw8(self):
    self.seg1()  
    self.seg2()
    self.seg3()
    self.seg4()
    self.seg5()
    self.seg6()
    self.seg7()
  
  def draw9(self):
    self.seg1()  
    self.seg2()
    self.seg3()
    self.seg4()    
    self.seg6()
    self.seg7()
    

  def seg1(self):
    self.dc.DrawLine(self.coor[0][0], self.coor[0][1], self.coor[1][0], self.coor[1][1])

  def seg2(self):
    self.dc.DrawLine(self.coor[0][0], self.coor[0][1], self.coor[2][0], self.coor[2][1])

  def seg3(self):
    self.dc.DrawLine(self.coor[1][0], self.coor[1][1], self.coor[3][0], self.coor[3][1])

  def seg4(self):
    self.dc.DrawLine(self.coor[2][0], self.coor[2][1], self.coor[3][0], self.coor[3][1])

  def seg5(self):
    self.dc.DrawLine(self.coor[2][0], self.coor[2][1], self.coor[4][0], self.coor[4][1])

  def seg6(self):
    self.dc.DrawLine(self.coor[3][0], self.coor[3][1], self.coor[5][0], self.coor[5][1])

  def seg7(self):
    self.dc.DrawLine(self.coor[4][0], self.coor[4][1], self.coor[5][0], self.coor[5][1])
