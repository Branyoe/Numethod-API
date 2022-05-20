
from src.models.FakeRuleOrder import FakeRuleOrder
from src.models.Process import Process
from src.utils import fxCalc

class IterationFakeRule:
    approxError = None

    def __init__(self, xLow, fxLow, xUp, fxUp, fx):
        self.fx = fx
        self.xLow = xLow
        self.fxLow = fxLow
        self.xUp = xUp
        self.fxUp = fxUp
        self.xRes = self.__fakeRuleCalc()
        self.fxRes = fxCalc(self.xRes, fx)
        self.process = {
            "fakeRule": self.processOfFakeRule()
        }
        
    def processOfFakeRule(self):
        return [
            {
                "t1": self.xUp,
                "t2": self.fxUp,
                "t3": self.xLow,
                "t4": self.xUp,
                "t5": self.fxLow,
                "t6": self.fxUp,
            },
            {
                "t1": self.xUp,
                "t2": self.fxUp,
                "t3": self.xLow - self.xUp,
                "t4": self.fxLow - self.fxUp
            },
            {
                "t1": self.xUp,
                "t2": self.fxUp * (self.xLow - self.xUp),
                "t3": self.fxLow - self.fxUp
            },
            {
                "t1": self.xUp,
                "t2": (self.fxUp * (self.xLow - self.xUp)) / (self.fxLow - self.fxUp)
            }
        ]

    def __fakeRuleCalc(self):
        return self.xUp - (self.fxUp * (self.xLow - self.xUp))/(self.fxLow - self.fxUp)

    def getNewOrder(self):
        if (self.getStopFactorFx()) < 0:
            return FakeRuleOrder(
                self.xLow,
                (self.fxLow / 2),
                self.xRes,
                self.fxRes,
                self.fx
            )
        else:
            return FakeRuleOrder(
                self.xRes,
                self.fxRes,
                self.xUp,
                (self.fxUp / 2),
                self.fx
            )

    def getStopFactorFx(self):
        return self.fxRes * self.fxLow

    def __str__(self):
        return f'xLow: {self.xLow}\nfxLow: {self.fxLow}\nxUp: {self.xUp}\nfxUp: {self.fxUp}\nxRes: {self.xRes}\nfxRes: {self.fxRes}\neApp: {self.approxError}'
