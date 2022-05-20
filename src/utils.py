# En este archivo se definen funciones de utilidad para cualquier proposito
# verifica que un reques sea valido mediante la comparacion de el reques recivido con el esperado
# devolviendo true o false respectivamente

def fxCalc(x, fx):
    fx = fx.strip().replace(" ", "").replace("x", str(x))
    return eval(fx)

def calcApproxError(xNew, xOld):
    try:
        res = ((xNew - xOld)/(xNew))*100
    except:
        return None
        
    if res < 0:
        return res*-1
    return res

def verifyRequest(data, spectedRequest):
    res = False
    if len(data) != len(spectedRequest):
        return False
    for itm in spectedRequest:
        if itm in data:
            res = True
        else:
            return False

    return res

# verifíca que el tipo de dato sea int o float en cada una de las propiedades de data y devuelve true
# de lo contrario devolverá false


def verifyType(data):
    res = False
    for itm in data:
        if type(data[itm]) is int or type(data[itm]) is float:
            res = True
        else:
            # autoríza que la propiedad trueValue pueda ser str o en su defecto int o float
            if itm == "trueValue" and type(data[itm]) is str:
                res = True
            else:
                return False

    return res


