import wx
import time
import threading
import random

from Bet import Bet
from DigitX import DigitX
from Light import Light
from FourDigits import Credit, Win
        


if __name__ == '__main__':
  app = wx.App()
  frame = wx.Frame(None, size=(800, 600))
  panel = wx.Panel(frame)
  panel.SetBackgroundColour(wx.Colour(0, 0, 32))

  # layout
  credit = Credit(panel, (0, 0))
  #win = Win(panel, (100, 0))

  # STM
  
  # sevices
  
  frame.Show()
  app.MainLoop()

