# -*- encoding: utf-8 -*-

import os

from app.core import Core

#: Creamos la aplicación
app = Core.create_app()

#: Cargamos los valores del archivo .env
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
if os.path.exists(dotenv_path):
    Core.load_dotenv(dotenv_path)
else:
    raise Exception('No existe el archivo .env')

#: Ejecutamos la aplicación
if __name__ == "__main__":
    app.run(debug=True)
