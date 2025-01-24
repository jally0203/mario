import threading
import random

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
    global state, lights, curLight, comparing_bet
    while True:
      if !self.flag:
        print('Comparing thread stop')
        break
      state = State.WAITING
      #if state == State.COMPARING:                      
      #  if comparing_bet == ord('a'):
      #    win *= 2
      #  else:
      #    win = 0
      #    state = State.WAITING
        
        
        
