# -*- encoding: utf-8 -*-

from app.core import Core

#: Creamos la aplicación
app = Core.create_app()

#: Ejecutamos la aplicación
if __name__ == "__main__":
    app.run(debug=True)
