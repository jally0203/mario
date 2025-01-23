import wx
import time
import threading
import random

from Bet import Bet
from DigitX import DigitX
from Light import Light
from FourDigits import Credit, Win
from State import State
from Running import Running

# items
bets = []
digitsH = []
digitsL = []
creditDigit = None
winDigit = None
lights = []
# vairables
betImgs = ['dog.png', 'man.png', 'dog.png', 'man.png', 'dog.png', 'man.png', 'dog.png', 'man.png']
awards = [5, 10, 15, 20, 20, 30, 40, 100]
keys = ['8', '7', '6', '5', '4', '3', '2', '1']
awards = [15, 20, 2, 0, 5, 2, 10, 20, 2, 40, 5, 2, 15, 30, 2, 0, 5, 2, 10, 20, 50, 100, 25, 5]
types = [5, 3, 3, 0, 7, 6, 6, 4, 1, 1, 7, 5, 5, 2, 2, 0, 7, 6, 6, 4, 0, 0, 0, 7]
# STM
state = State.WAITING
# bet and win
playBet = []
credit = 10
win = 0
    
def putBet():
  for i in range(8):
    bets.append(Bet(panel, betImgs[i], awards[i], keys[i]))
    digitsH.append(DigitX(panel, (1620+10, i*132+10+16+50)))    
    digitsL.append(DigitX(panel, (1620+10, i*132+10+16)))
    bets[i].SetSize((185, 126))
    bets[i].SetPosition((1720+7, i*132+10+6))
    bets[i].setDigitH(digitsH[i])
    bets[i].setDigitL(digitsL[i])
            
def putFourDigits():        
  creditDigit = Credit(panel, (340, 200))
  winDigit = Win(panel, (340, 600))
  creditDigit.setNum(credit)
  winDigit.setNum(win)
  
def putLight():
  bitmap_off = wx.Bitmap('off.png', wx.BITMAP_TYPE_ANY)
  bitmap_on = wx.Bitmap('on.png', wx.BITMAP_TYPE_ANY)
  for i in range(6):
    lights.append(Light(panel, bitmap_on, bitmap_off, (i*220+120, 80)))
  for i in range(6):
    lights.append(Light(panel, bitmap_on, bitmap_off, (6*220+120, i*130+80)))
  for i in range(6, 0, -1):
    lights.append(Light(panel, bitmap_on, bitmap_off, (i*220+120, 6*130+80)))
  for i in range(6, 0, -1):
    lights.append(Light(panel, bitmap_on, bitmap_off, (120, i*130+80)))
  for i in range(24):
    lights[i].setAward(awards[i])
    lights[i].setType(types[i])
    
def getPlayBet():
  global playBet
  playBet = []
  for i in range(7, -1, -1):
    playBet.append(bets[i].getBet())
  return playBet  

def onKeyDown(evt):
  global state
  if evt.GetKeyCode() == wx.WXK_SPACE or evt.GetKeyCode() == wx.WXK_RETURN:
    if state == State.WAITING:
      print('bet: ', getPlayBet())
      if sum(getPlayBet()) > 0:
        state = State.RUNNING    
  elif evt.GetKeyCode() == ord('q') or evt.GetKeyCode() == ord('Q'):
    running_thread.disable()
    flashing_thread.disable()
    frame.Close()
  else:
    if state == State.WAITING:
      for i in range(8):
        bets[i].patch(evt)


if __name__ == '__main__':
  app = wx.App()
  frame = wx.Frame(None, size=(800, 600))
  panel = wx.Panel(frame)
  panel.SetBackgroundColour(wx.Colour(0, 0, 32))

  # layout
  putBet()
  putLight()
  putFourDigits()
  bets[0].SetFocus()
  bets[0].Bind(wx.EVT_KEY_DOWN, onKeyDown)  

  # threads
  running_thread = Running()
  running_thread.start()
  flashing_thread = Flashing()
  flashing_thread.start()
  comparing_thread = Comparing()
  comparing_thread.start()
  
  # sevices
  frame.ShowFullScreen(True)
  frame.Show()
  app.MainLoop()

