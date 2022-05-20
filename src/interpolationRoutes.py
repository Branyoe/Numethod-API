# este archivo define todas las rutas para el blueprint routes

# Importaciones******************************************
# desde librerias
from flask import Blueprint, jsonify, request

# desde el proyecto
from src.interpolationControllers import lagrangeIntMethod, linearIntMethod, newtonIntMethod
from src.utils import verifyRequest, verifyType

# definicion de mensajes de error******************************************
badRequestMessage = {"Error": "invalid reques"}
notFoundRequestMessage = {"Error": "nonexistent request"}

# inclución de el Blueprint operations******************************************
operations = Blueprint('operations', __name__)

# definicion de ruta linear-interpolation******************************************
@operations.route('/linear-interpolation', methods=['POST'])
def linearInt():
    data = request.json
    # verifica que data sea un diccionario******************************************
    if(type(data) is not dict) : return jsonify(notFoundRequestMessage)
    spectedRequest = ["x0", "fx0", "x1", "fx1", "x", "trueValue"]
    # verifica que se aprueben los filtros
    if verifyRequest(data, spectedRequest) and verifyType(data):
        return jsonify({"res": linearIntMethod(data)})
    else:
        return jsonify(badRequestMessage)

# definicion de ruta linear-interpolation******************************************
@operations.route('lagrange-interpolation', methods=['POST'])
def lagrangeInt():
    data = request.json
    # verifica que data sea un diccionario
    if(type(data) is not dict) : return jsonify(notFoundRequestMessage)
    spectedRequest = ["x0", "fx0", "x1", "fx1", "x2", "fx2", "x", "trueValue"]
    # verifica que se aprueben los filtros
    if verifyRequest(data, spectedRequest) and verifyType(data):
        return jsonify({"res": lagrangeIntMethod(data)})
    else:
        return jsonify(badRequestMessage)

# definicion de ruta newton-interpolation******************************************
@operations.route('newton-interpolation', methods=['POST'])
def newtonInt():
    data = request.json
    # verifica que data sea un diccionario
    if(type(data) is not dict) : return jsonify(notFoundRequestMessage)
    spectedRequest = ["x0", "fx0", "x1", "fx1", "x2", "fx2", "x", "trueValue"]
    # verifica que se aprueben los filtros
    if verifyRequest(data, spectedRequest) and verifyType(data):
        return jsonify({"res": newtonIntMethod(data)})
    else:
        return jsonify(badRequestMessage)
