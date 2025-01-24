import threading
import random

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
    global state, lights, curLight
    while True:
      if !self.flag:
        print('Running thread stop')
        break
      if state == State.RUNNING:
        target = random.randint(0, 23)
        step = random.randint(180, 200)
        #print('before running: target', target, 'step', step, 'cur', curLight)
        n = step
        while n > 0:
          n -= 1
          curLight += 1
          curLight %= 24
          lights[curLight].set()
          time.sleep(0.03)
          lights[curLight].clear()
        while curLight != target:
          curLight += 1
          curLight %= 24
          lights[curLight].set()
          time.sleep(0.3)
          lights[curLight].clear()
        lights[curLight].set()
        #print('after running: target', target, 'step', step, 'cur', curLight)  
        state = State.FLASHING
       
