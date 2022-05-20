# este archivo es el principal y se enmcarga de correr la app

# Importaciones
from src import createApp

# Instacia app
app = createApp()

# verifica que el modulo estén en main y lo ejecuta
if __name__ == '__main__':
    app.run(debug=True)
    