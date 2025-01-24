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
    return award * gv.palyBet[mtype]
    
  def run(self):
    print('Flashing is running')
    while True:
      time.sleep(0.1)
      if not self.flag:
        print('Flashing thread stop')
        break
      while gv.state == State.FLASHING:
        if self.getWinning() > 0:                     
          gv.lights[gv.curLight].set()
          time.sleep(0.1)
          gv.lights[gv.curLight].clear()
          time.sleep(0.1)
        else:
          gv.reset_flag = True
          gv.state = State.WAITING
      
            
