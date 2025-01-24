import wx
import time
import threading
import random

import global_var as gv
from Bet import Bet
from DigitX import DigitX
from Light import Light
from FourDigits import Credit, Win
from State import State
from Running import Running
from Flashing import Flashing
from Comparing import Comparing

def putBet():
  for i in range(8):
    gv.bets.append(Bet(panel, gv.betImgs[i], gv.awards[i], gv.keys[i]))
    gv.digitsH.append(DigitX(panel, (1620+10, i*132+10+16+50)))    
    gv.digitsL.append(DigitX(panel, (1620+10, i*132+10+16)))
    gv.bets[i].SetSize((185, 126))
    gv.bets[i].SetPosition((1720+7, i*132+10+6))
    gv.bets[i].setDigitH(gv.digitsH[i])
    gv.bets[i].setDigitL(gv.digitsL[i])
            
def putFourDigits():        
  gv.creditDigit = Credit(panel, (340, 200))
  gv.winDigit = Win(panel, (340, 600))
  gv.creditDigit.setNum(gv.credit)
  gv.winDigit.setNum(gv.win)
  
def collect_winning():
  gv.credit += gv.win
  gv.win = 0
  gv.winDigit.setNum(gv.win)
  gv.creditDigit.setNum(gv.credit)
  
def putLight():
  bitmap_off = wx.Bitmap('off.png', wx.BITMAP_TYPE_ANY)
  bitmap_on = wx.Bitmap('on.png', wx.BITMAP_TYPE_ANY)
  for i in range(6):
    gv.lights.append(Light(panel, bitmap_on, bitmap_off, (i*220+120, 80)))
  for i in range(6):
    gv.lights.append(Light(panel, bitmap_on, bitmap_off, (6*220+120, i*130+80)))
  for i in range(6, 0, -1):
    gv.lights.append(Light(panel, bitmap_on, bitmap_off, (i*220+120, 6*130+80)))
  for i in range(6, 0, -1):
    gv.lights.append(Light(panel, bitmap_on, bitmap_off, (120, i*130+80)))
  for i in range(24):
    gv.lights[i].setAward(gv.awards[i])
    gv.lights[i].setType(gv.types[i])
    
def getPlayBet():
  gv.playBet = []
  for i in range(7, -1, -1):
    gv.playBet.append(gv.bets[i].getBet())
  return gv.playBet  

def onKeyDown(evt):
  if evt.GetKeyCode() == wx.WXK_SPACE or evt.GetKeyCode() == wx.WXK_RETURN:    
    if gv.state == State.WAITING:
      gv.reset_flag = False
      #print('bet: ', getPlayBet())      
      if sum(getPlayBet()) > 0:
        gv.state = State.RUNNING  
    elif gv.state == State.FLASHING:
      collect_winning()
      gv.state = State.WAITING
  elif evt.GetKeyCode() == ord('q') or evt.GetKeyCode() == ord('Q'):
    running_thread.disable()
    flashing_thread.disable()
    comparing_thread.disable()
    frame.Close()
  elif evt.GetKeyCode() == ord('a') or evt.GetKeyCode() == ord('l'):
    if gv.state == State.FLASHING:
      gv.comparing_bet = evt.GetKeyCode()
      gv.state = State.COMPARING      
  else:
    if gv.state == State.WAITING:
      if gv.reset_flag:
        gv.playBet = []
        for i in range(8):
          gv.bets[i].clearBet()
        gv.reset_flag = False  
      for i in range(8):
        gv.bets[i].patch(evt)


if __name__ == '__main__':
  app = wx.App()
  frame = wx.Frame(None, size=(800, 600))
  panel = wx.Panel(frame)
  panel.SetBackgroundColour(wx.Colour(0, 0, 32))
  state = State.WAITING

  # layout
  putBet()
  putLight()
  putFourDigits()
  gv.bets[0].SetFocus()
  gv.bets[0].Bind(wx.EVT_KEY_DOWN, onKeyDown)  

  # threads, assume there's a token pass through 3 threads
  running_thread = Running()
  running_thread.start()
  flashing_thread = Flashing()
  flashing_thread.start()
  comparing_thread = Comparing()
  comparing_thread.start()
  
  # sevices
  #frame.ShowFullScreen(True)
  frame.Show()
  app.MainLoop()

