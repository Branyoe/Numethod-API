# este archivo define las funciones que ejecutarán las rutas del archivo operations

# calcula el error verdadero

def trueError(trueValue, approxValue):
    return trueValue - approxValue

# calcula el error relativo porcentual


def percentRelativeError(trueError, trueValue):
    return ((trueError / trueValue) * 100)

# calcula una interpolacion mediante el metodo lineal


def linearIntMethod(data):
    values = []
    process = []
    res = {}
    for v in data:
        values.append(data[v])
    x0, fx0, x1, fx1, x, trueValue = values
    # fx = fx0 + ( fx1 - fx0 / x1 - x0)( x - x0 )

    process.append({
        "t1": fx0,
        "t2": fx1 - fx0,
        "t3": x1 - x0,
        "t4": x - x0 
    })
    segm1 = fx0
    segm2 = (fx1 - fx0) / (x1 - x0)
    segm3 = x - x0
    process.append({
        "t1": fx0,
        "t2": segm2,
        "t3": segm3, 
    })

    process.append({
        "t1": fx0,
        "t2": segm2 * segm3
    })

    fx = segm1 + segm2 * segm3
    if type(trueValue) is float or type(trueValue) is int:
        res = {
            "fx": fx,
            "trueError": trueError(trueValue, fx),
            "percentRelativeError": percentRelativeError(trueError(trueValue, fx), trueValue),
            "process": process
        }
    else:
        res = {
            "fx": fx,
        }

    return res

# calcula una interpolacion mediante el metodo lagrange
def lagrangeIntMethod(data):
    values = []
    process = []
    for v in data:
        values.append(data[v])
    x0, fx0, x1, fx1, x2, fx2, x, trueValue = values

    process.append({
        "t1": {
            "numerador": {
                "t1": x - x1,
                "t2": x - x2
            },
            "denominador": {
                "t1": x0 - x1,
                "t2": x0 - x2
            }
        },
        "t2": fx0,
        "t3": {
            "numerador": {
                "t1": x - x0,
                "t2": x - x2
            },
            "denominador": {
                "t1": x1 - x0,
                "t2": x1 - x2
            }
        },
        "t4": fx1,
        "t5": {
            "numerador": {
                "t1": x - x0,
                "t2": x - x1
            },
            "denominador": {
                "t1": x2 - x0,
                "t2": x2 - x1
            }
        },
        "t6": fx2
    })

    process.append({
        "t1": {
            "numeradorN": (x-x1)*(x-x2),
            "denominadorN": (x0-x1) * (x0-x2)
        },
        "t2": fx0,
        "t3": {
            "numeradorN": (x-x0) * (x-x2),
            "denominadorN": (x1-x0) * (x1-x2)
        },
        "t4": fx1,
        "t5": {
            "numeradorN": (x-x0) * (x-x1),
            "denominadorN": (x2-x0) * (x2-x1)
        },
        "t6": fx2
    })

    process.append({
        "t1N": ((x-x1)*(x-x2))/((x0-x1) * (x0-x2)),
        "t2": fx0,
        "t3N": ((x-x0) * (x-x2))/((x1-x0) * (x1-x2)),
        "t4": fx1,
        "t5N": ((x-x0) * (x-x1))/((x2-x0) * (x2-x1)),
        "t6": fx2
    })

    process.append({
        "t1N": (((x-x1)*(x-x2))/((x0-x1) * (x0-x2)))*fx0,
        "t2": (((x-x0) * (x-x2))/((x1-x0) * (x1-x2)))*fx1,
        "t3N": (((x-x0) * (x-x1))/((x2-x0) * (x2-x1)))*fx2
    })

    process.append({
        "t1N": (((x-x1)*(x-x2))/((x0-x1) * (x0-x2)))*fx0 + (((x-x0) * (x-x2))/((x1-x0) * (x1-x2)))*fx1 + (((x-x0) * (x-x1))/((x2-x0) * (x2-x1)))*fx2
    })

    segm1 = ((x-x1)*(x-x2))/((x0-x1)*(x0 - x2))*fx0
    segm2 = ((x-x0)*(x-x2))/((x1-x0)*(x1 - x2))*fx1
    segm3 = ((x-x0)*(x-x1))/((x2-x0)*(x2 - x1))*fx2

    f2x = segm1 + segm2 + segm3

    if type(trueValue) is float or type(trueValue) is int:
        res = {
            "f2x": f2x,
            "trueError": trueError(trueValue, f2x),
            "percentRelativeError": percentRelativeError(trueError(trueValue, f2x), trueValue),
            "process": process
        }
    else:
        res = {
            "f2x": f2x,
        }
    
    return res

#   calcula una interpolacion mediante el metodo Newton
def newtonIntMethod(data):
    values = []
    bB = []
    b1 = []
    b2 = []
    processF2x = []
    for v in data:
        values.append(data[v])
    x0, fx0, x1, fx1, x2, fx2, x, trueValue = values
    

    b = []
    b.append(fx0)
    b.append( ( fx1 - fx0 ) / ( x1- x0 ) )
    b.append( ( (( fx2 - fx0 ) / ( x2 - x0 )) - (( fx1 - fx0 ) / ( x1 - x0 )) ) / (x2 - x1) )

    bB = b;
    b1.append({
        "t1": fx1 - fx0,
        "t2": x1 - x0
    })

    b1.append({
        "t1": (fx1 - fx0)/ ( x1 - x0 )
    })

    b2.append({
        "t1": fx2 - fx0,
        "t2": x2 - x0,
        "t3": fx1 - fx0,
        "t4": x1 - x0,
        "t5": x2 - x1
    })
    b2.append({
        "t1": (fx2 - fx0)/(x2 - x0),
        "t2": (fx1 - fx0)/ ( x1 - x0 ),
        "t3": x2 - x1
    })

    processF2x.append({
        "t1": bB[0],
        "t2": bB[1],
        "t3": x - x0,
        "t4": bB[2],
        "t5": x - x0,
        "t6": x - x1
    })

    processF2x.append({
        "t1": bB[0],
        "t2": bB[1] * (x-x0),
        "t3": bB[2] * (x-x0) * (x-x1)
    })

    
    f2x = b[0] + b[1] * (x - x0) + b[2] * (x - x0) * (x - x1);

    if type(trueValue) is float or type(trueValue) is int:
        res = {
            "f2x": f2x,
            "processF2x": processF2x,
            "bB": bB,
            "b1": b1,
            "b2": b2,
            "trueError": trueError(trueValue, f2x),
            "percentRelativeError": percentRelativeError(trueError(trueValue, f2x), trueValue)
        }
    else:
        res = {
            "f2x": f2x,
        }

    return res
