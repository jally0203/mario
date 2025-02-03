import threading
import time

import global_var as gv
from State import State

class Flashing(threading.Thread):

  def __init__(self):
    threading.Thread.__init__(self)
    self.flag = True
    
  def enable(self):
    self.flag = True
    
  def disable(self):
    self.flag = False
    
  def getWinning(self):  
    award = gv.lights[gv.curLight].getAward()
    mtype = gv.lights[gv.curLight].getType()
    print('Flashing: award', award, 'mtype', mtype, 'winning', award * gv.playBet[mtype])
    gv.winDigit.setNum(award * gv.playBet[mtype])
    return award * gv.playBet[mtype]
    
  def run(self):
    print('Flashing is running')
    while True:
      time.sleep(0.1)
      if not self.flag:
        print('Flashing thread stop')
        break
      if gv.state == State.FLASHING:
        print('Flashing got the ball')
        if self.getWinning() > 0:     
          while self.flag:
            gv.lights[gv.curLight].set()
            time.sleep(0.1)
            gv.lights[gv.curLight].clear()
            time.sleep(0.1)
        else:
          gv.reset_flag = True
          gv.state = State.WAITING
      
            
