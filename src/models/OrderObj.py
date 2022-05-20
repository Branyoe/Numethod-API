class OrderObj:
  def __init__(self, xLow, xUp, fx):
    self.xLow = xLow
    self.xUp = xUp
    self.fx = fx
  
  def __str__(self):
        return f'xLow: {self.xLow}\nxUp: {self.xUp}\nfx: {self.fx}'