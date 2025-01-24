import threading
import random
import time

import global_var as gv
from State import State

class Running(threading.Thread):

  def __init__(self):
    threading.Thread.__init__(self)
    self.flag = True
    
  def enable(self):
    self.flag = True
    
  def disable(self):
    self.flag = False
    
  def run(self):
    print('Running is running')
    while True:
      time.sleep(0.1)
      if not self.flag:
        print('Running thread stop')
        break
      if gv.state == State.RUNNING:
        print('Running got the ball')
        target = random.randint(0, 23)
        step = random.randint(180, 200)
        n = step
        while n > 0:
          n -= 1
          gv.curLight += 1
          gv.curLight %= 24
          gv.lights[gv.curLight].set()
          time.sleep(0.03)
          gv.lights[gv.curLight].clear()
        while gv.curLight != target:
          gv.curLight += 1
          gv.curLight %= 24
          gv.lights[gv.curLight].set()
          time.sleep(0.3)
          gv.lights[gv.curLight].clear()
        gv.lights[gv.curLight].set()
        print('Running : target', target, 'step', step, 'cur', gv.curLight)  
        gv.state = State.FLASHING
       
