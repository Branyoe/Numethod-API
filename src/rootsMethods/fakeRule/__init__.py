from src.models.IterationFakeRule import IterationFakeRule

from src.utils import calcApproxError, fxCalc


def fakeRule(fx, xLow, xUp, stopFactor):
    iterations = []
    i = 0
    fxLow = fxCalc(xLow, fx)
    fxUp = fxCalc(xUp, fx)

    while True:
      currentIteration = IterationFakeRule(
        xLow,
        fxLow,
        xUp,
        fxUp,
        fx
      )
      iterations.append(currentIteration.__dict__)

      if i > 0:
        iterations[i]["approxError"] = calcApproxError(currentIteration.xRes, iterations[i-1]["xRes"])
        if currentIteration.approxError:
          if currentIteration.approxError <= stopFactor:
            return iterations
      
      newData = currentIteration.getNewOrder()
      if newData is None: return { "message": "Intervalo fuera de rango"}
      xLow = newData.xLow
      fxLow = newData.fxLow
      xUp = newData.xUp
      fxUp = newData.fxUp
      i += 1
