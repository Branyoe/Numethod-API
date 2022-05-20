from src.models.Iteration import Iteration
from src.utils import calcApproxError


def bisection(data):
    # destructura la data
    values = []
    for v in data:
        values.append(data[v])
    fx, xLow, xUp, stopFactor = values

    iterations = []
    i = 0
    while True:
        iteration = Iteration(xLow, xUp, fx)
        iterations.append(iteration.__dict__)

        if(i > 0): 
            eApp = calcApproxError(iteration.xRes, iterations[i-1]["xRes"])
            iterations[i]["eApp"] = eApp
            eApp = 101 if eApp is None else eApp
            if eApp <= stopFactor:
                return iterations
        newData = iteration.getNewOrder()
        if newData is None:
            return {"message": "Intervalo fuera de rango"}
        fx = newData.fx
        xLow = newData.xLow
        xUp = newData.xUp
        i += 1