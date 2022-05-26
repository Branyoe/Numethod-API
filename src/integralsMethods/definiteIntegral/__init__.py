from sympy import integrate, latex, sqrt, pi
from sympy.abc import x


def definiteIntegral(fx, xLow, xUp):
    print(integrate(fx, (x, xLow, xUp)))
    obj = {
        "resultFrac": str(integrate(fx, (x, xLow, xUp))),
        "resultFloat": eval(str(integrate(fx, (x, xLow, xUp)))),
        "process": latex(integrate(fx, x))
    }
    return obj
