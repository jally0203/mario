import threading

from State import State

class Comparing(threading.Thread):

  def __init__(self):
    threading.Thread.__init__(self)
    self.flag = True
    
  def enable(self):
    self.flag = True
    
  def disable(self):
    self.flag = False
    
  def run(self):
    global state, lights, curLight
    while True:
      if !self.flag:
        print('Flashing thread stop')
        break
      if state == State.FLASHING:                      
        lights[curLight].set()
        time.sleep(0.1)
        lights[curLight].clear()
        time.sleep(0.1)
