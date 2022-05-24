#imports

from flask import Blueprint, request, jsonify
from src.integralsMethods.definiteIntegral import definiteIntegral

from src.utils import verifyRequest

# definición de blueprint para los metodos de raices
integralsMethods = Blueprint('integralsMethods', __name__)

@integralsMethods.route('definiteIntegral', methods=['POST'])
def definiteIntegralMethod():
  return definiteIntegral(request.json)