import threading

from State import State

class STM(threading.Thread):

  def __init__(self):
    threading.Thread.__init__(self)
    self.flag = False
    
  def enable(self):
    self.flag = True
    
  def disable(self):
    self.flag = False
    
  def run(self):
    while True:
      if !self.flag:
        break
      match(  
