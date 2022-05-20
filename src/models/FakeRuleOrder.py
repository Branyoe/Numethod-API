class FakeRuleOrder:
  def __init__(self, xLow, fxLow, xUp, fxUp, fx):
    self.xLow = xLow
    self.fxLow = fxLow
    self.xUp = xUp
    self.fxUp = fxUp
    self.fx = fx
  
  def __str__(self):
        return f'xLow: {self.xLow}\nfxLow: {self.fxLow}\nxUp: {self.xUp}\nfxUp: {self.fxUp}\nfx: {self.fx}'