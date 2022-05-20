#imports

from flask import Blueprint, jsonify, request

from src.rootsMethods.bisection import bisection
from src.rootsMethods.fakeRule import fakeRule

from src.utils import verifyRequest

# definición de blueprint para los metodos de raices
rootsMethods = Blueprint('rootsMethods', __name__)

# definición de errores
errors = {
  "Error1": {
    "Error": "invalid request",
  },
  "Error2": {
    "Error2": "nonexistent request"
  }
}


#*********Rutas****************************

# Ping
@rootsMethods.route('ping', methods=['GET'])
def ping():
  response = {
    "message": 'pong'
  }
  return jsonify(response) 

# Regla falsa
@rootsMethods.route('fake-rule', methods=['POST'])
def fakeRuleMethod():
  dataRequest = request.json 

  if(type(dataRequest) is not dict): return jsonify(errors["Error1"]);

  spectedDataRequest = ["fx", "xLow", "xUp", "stopFactor"]

  if verifyRequest(dataRequest, spectedDataRequest) is False:
    return jsonify(errors["Error1"])
  
  return jsonify(fakeRule(**dataRequest))
  
# Bisección
@rootsMethods.route('bisection', methods=['POST'])
def bisectionMethod():
  dataRequest = request.json

  if(type(dataRequest) is not dict): return jsonify(errors["Error1"]);

  spectedDataRequest = ["fx", "xLow", "xUp", "stopFactor"]
  if verifyRequest(dataRequest, spectedDataRequest):
    return jsonify(bisection(dataRequest))
  else:
    return jsonify(errors["Error1"])