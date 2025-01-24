import threading
import random
import time

import global_var as gv
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
    print('Comparing is running')
    while True:
      time.sleep(0.1)
      if not self.flag:
        print('Comparing thread stop')
        break
      gv.state = State.WAITING

        
        
        
