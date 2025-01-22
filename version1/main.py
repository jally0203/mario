import wx
import time
import threading
import random

from Bet import Bet
from DigitX import DigitX
from Light import Light

#  0  1  2  3  4  5  6
# 23                 7
# 22                 8
# 21                 9
# 20                10
# 19                11
# 18 17 16 15 14 13 12

betImgs = ['dog.png', 'man.png', 'dog.png', 'man.png', 'dog.png', 'man.png', 'dog.png', 'man.png']
awards = [5, 10, 15, 20, 20, 30, 40, 100]
keys = ['8', '7', '6', '5', '4', '3', '2', '1']
awards = [15, 20, 2, 0, 5, 2, 10, 20, 2, 40, 5, 2, 15, 30, 2, 0, 5, 2, 10, 20, 50, 100, 25, 5]
fruits = [5, 3, 3, 0, 7, 6, 6, 4, 1, 1, 7, 5, 5, 2, 2, 0, 7, 6, 6, 4, 0, 0, 0, 7]
bets = []
digitsL = []
digitsH = []
lights = []
playbet = []
bitmap_on = None
bitmap_off = None
state = 0
frame = None
thread_flag = True
curLight = 0
flash_flag = False
digitWin = []
digitCredit = []
win = 0
credit = 0

def onKeyDown(evt):
  global state, thread_flag, flash_flag, credit, win
  if evt.GetKeyCode() == wx.WXK_SPACE or evt.GetKeyCode() == wx.WXK_RETURN:
    if state == 0:
      print('bet: ', getPlayBet())
      if sum(getPlayBet()) > 0:
        state = 1
    elif state == 3:  
      flash_flag = False
      credit += win
      win = 0
      updateWin()
      updateCredit()
      state = 0  
  elif evt.GetKeyCode() == ord('q') or evt.GetKeyCode() == ord('Q'):
    thread_flag = False
    flash_flag = False
    frame.Close()
  else:
    if state == 0:
      for i in range(8):
        bets[i].patch(evt)

def getPlayBet():
  global playBet
  playBet = []
  for i in range(7, -1, -1):
    playBet.append(bets[i].getBet())
  return playBet  

def putBet():
  for i in range(8):
    bets.append(Bet(panel, betImgs[i], awards[i], keys[i]))
    digitsH.append(DigitX(panel, (1620+10, i*132+10+16+50)))    
    digitsL.append(DigitX(panel, (1620+10, i*132+10+16)))
    bets[i].SetSize((185, 126))
    bets[i].SetPosition((1720+7, i*132+10+6))
    bets[i].setDigitH(digitsH[i])
    bets[i].setDigitL(digitsL[i])

def putLight2():
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
    lights[i].setPair(awards[i], fruits[i])

def putWinNCredit():
  global digitWin, digitCredit
  for i in range(4):
    digitWin.append(DigitX(panel, (340, 700-i*50)))
  for i in range(4):
    digitCredit.append(DigitX(panel, (340, 400-i*50)))
    
def updateWin():
  vs = str(win)
  if win >= 1000:    
    digitWin[0].update(int(vs[0]))
    digitWin[1].update(int(vs[1]))
    digitWin[2].update(int(vs[2]))
    digitWin[3].update(int(vs[3]))
  elif win >= 100:    
    digitWin[0].update(0)
    digitWin[1].update(int(vs[0]))
    digitWin[2].update(int(vs[1]))
    digitWin[3].update(int(vs[2]))  
  elif win >= 10:    
    digitWin[0].update(0)
    digitWin[1].update(0)
    digitWin[2].update(int(vs[0]))
    digitWin[3].update(int(vs[1]))  
  else:    
    digitWin[0].update(0)
    digitWin[1].update(0)
    digitWin[2].update(0)
    digitWin[3].update(int(vs[0]))  
    
    
def updateCredit():
  vs = str(credit)
  if credit >= 1000:    
    digitCredit[0].update(int(vs[0]))
    digitCredit[1].update(int(vs[1]))
    digitCredit[2].update(int(vs[2]))
    digitCredit[3].update(int(vs[3]))
  elif credit >= 100:    
    digitCredit[0].update(0)
    digitCredit[1].update(int(vs[0]))
    digitCredit[2].update(int(vs[1]))
    digitCredit[3].update(int(vs[2]))  
  elif credit >= 10:    
    digitCredit[0].update(0)
    digitCredit[1].update(0)
    digitCredit[2].update(int(vs[0]))
    digitCredit[3].update(int(vs[1]))  
  else:    
    digitCredit[0].update(0)
    digitCredit[1].update(0)
    digitCredit[2].update(0)
    digitCredit[3].update(int(vs[0]))      
    
def allLightOn():
  for i in range(24):
    lights[i].set()

def allLightOff():
  for i in range(24):
    lights[i].clear()
    
def lightOn(n):  
  lights[n].set()   

def lightOff(n):  
  lights[n].clear()   
 
def flash(): 
  while flash_flag:
    lightOff(curLight)
    time.sleep(0.1)
    lightOn(curLight)  
    time.sleep(0.1)
   
#def lightRunOneCycle(start, speed):
#  global curLight
#  allLightOff()
#  for i in range(start, start + 24):
#    curLight = i % 24
#    lightOn(curLight)
#    time.sleep(speed)
#    lightOff(curLight)

def STM2():
  global curLight, state, flash_flag, win
  while(thread_flag):
    #print(state)
    match(state):
      case 0:    # waiting
        pass        
      case 1:    # running
        target = random.randint(0, 23)
        step = random.randint(180, 200)
        print('before running: target', target, 'step', step, 'cur', curLight)
        n = step
        while n > 0:
          n -= 1
          curLight += 1
          curLight %= 24
          lightOn(curLight)
          time.sleep(0.03)
          lightOff(curLight)
        while curLight != target:
          curLight += 1
          curLight %= 24
          lightOn(curLight)
          time.sleep(0.3)
          lightOff(curLight)
        lightOn(curLight)
        print('after running: target', target, 'step', step, 'cur', curLight)  
        state = 2
      case 2:   # flashing
        print('state 2')
        award, fruit = lights[curLight].getPair()
        win = award * playBet[fruit]
        print('award', award, 'fruit', fruit, 'total', win)
        flash_flag = True        
        thread_flash = threading.Thread(target = flash)
        thread_flash.start()
        state = 3
      case 3:    # comparing
        pass
      case 4:    # collectin  
        pass
        
        
                
  print('thread stop')          


app = wx.App()
frame = wx.Frame(None, size=(800, 600))
panel = wx.Panel(frame)
panel.SetBackgroundColour(wx.Colour(0, 0, 32))

# layout
putBet()
putLight2()
putWinNCredit()
bets[0].SetFocus()
bets[0].Bind(wx.EVT_KEY_DOWN, onKeyDown)    

credit = 10
updateCredit()

# STM
thread_stm = threading.Thread(target = STM2)
thread_stm.start()

frame.ShowFullScreen(True)
frame.Show()
app.MainLoop()

