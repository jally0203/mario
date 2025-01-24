import threading

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
    global lights, curLight, playBet
    self.award = lights[curLight].getAward()
    self.mtype = lights[curLight].getType()
    return self.award * palyBet[self.mtype]
    
  def run(self):
    global state, lights, curLight, reset_flag
    while True:
      if !self.flag:
        print('Flashing thread stop')
        break
      if state == State.FLASHING:
        if self.getWinning() > 0:                     
          lights[curLight].set()
          time.sleep(0.1)
          lights[curLight].clear()
          time.sleep(0.1)
        else:
          reset_flag = True
          state = State.WAITING
      
            
