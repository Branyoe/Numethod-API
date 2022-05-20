from src.models.OrderObj import OrderObj
from src.models.ProcessBisection import ProcessBisection

class Iteration:
    eApp = None

    def __init__(self, xLow, xUp, fx):
        self.fx = fx
        self.xLow = xLow
        self.fxLow = self.__fxCalc(xLow)
        self.xUp = xUp
        self.fxUp = self.__fxCalc(xUp)
        self.xRes = self.__bisectionCalc()
        self.fxRes = self.__fxCalc(self.xRes)
        self.process = ProcessBisection(
            self.procesOfBisection()
        ).__dict__

    def __fxCalc(self, x):
        fx = self.fx.strip()
        fx = self.fx.replace(" ", "")
        fx = self.fx.replace("x", str(x))
        return eval(fx)

    def procesOfBisection(self):
        return [
            {
                "t1": self.xLow,
                "t2": self.xUp,
            },
            {
                "t1": self.xLow + self.xUp
            }
        ]

    def __bisectionCalc(self):
        return (self.xLow + self.xUp) / 2

    def getNewOrder(self):
        if(self.fxRes < 0 and self.fxLow > 0):
            return OrderObj(self.xRes, self.xLow, self.fx)
        if(self.fxRes > 0 and self.fxLow < 0):
            return OrderObj(self.xLow, self.xRes, self.fx)
        if(self.fxRes < 0 and self.fxUp > 0):
            return OrderObj(self.xRes, self.xUp, self.fx)
        if(self.fxRes > 0 and self.fxUp < 0):
            return OrderObj(self.xUp, self.xRes, self.fx)

    def __str__(self):
        return f'xLow: {self.xLow}\nfxLow: {self.fxLow}\nxUp: {self.xUp}\nfxUp: {self.fxUp}\nxRes: {self.xRes}\nfxRes: {self.fxRes}\neApp: {self.eApp}'
