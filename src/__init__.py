#este archivo crea el modelo de la aplicación/servidor

# importaciones
from flask import Flask
from flask_cors import CORS


# define una funcion la cual crea la app
def createApp():
    app = Flask(__name__)
    CORS(app)

    app.config['SECRET_KEY'] = 'wadagugu'

    from .interpolationRoutes import operations
    from .rootsMethods.rootsMethodsRoutes import rootsMethods

    app.register_blueprint(operations, url_prefix=('/api/'))
    app.register_blueprint(rootsMethods, url_prefix=('/api/rootsMethods/'))
    return app
    