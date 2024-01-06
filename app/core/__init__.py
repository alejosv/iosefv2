# -*- encoding: utf-8 -*-

import os
import requests

from os import path

from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
# from flask_ipban import IpBan

class Core():

    app: Flask = None

    @staticmethod
    def create_app() -> Flask:

        #: Obtenemos el nombre del directorio del proyecto que esta dos niveles arriba del directorio actual
        project_path = path.dirname(path.dirname(__file__))

        #: Creamos la aplicación
        Core.app = Flask(
            __name__,
            template_folder=path.join(project_path, 'templates'),
            static_folder=path.join(project_path, 'static'),
            static_url_path='/static'
        )

        #: Hacemos un GET a la URL https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/firehol_level1.netset para obtener la lista de IPs bloqueadas
        # black_list = requests.get('https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/firehol_level1.netset').text.split('\n')


        #: Configuramos la aplicación
        Core.app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
        Core.app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
        Core.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Core.str_to_bool(os.environ['SQLALCHEMY_TRACK_MODIFICATIONS'])
        Core.app.config['SQLALCHEMY_ECHO'] = Core.str_to_bool(os.environ['SQLALCHEMY_ECHO'])

        #: Inicializamos el IpBan
        #ip_ban = IpBan(
        #    persist=True,
        #    abuse_IPDB_config=dict(key='98c6a2386fd34e0e79f6b140f87ce23e10158a549b13e02360b1a3a963b6a06faa479a21c1f56233')
        #)
        #ip_ban.init_app(Core.app)

        #: Agregamos las IPs a la lista negra
        #for ip in black_list:
        #    ip_ban.block(ip, 'blacklist', 'IP bloqueada por el sistema')

        #: Inicializamos el LoginManager
        login_manager = LoginManager()

        #: Inicializamos el LoginManager
        login_manager.init_app(Core.app)

        #: Definimos la función que carga el usuario
        @login_manager.user_loader
        def load_user(user_id):
            return None
        

        #: Obtenemos el directorio de los módulos
        modules_path = path.join(project_path, 'modules')
        Core.load_modules(Core.app, modules_path)

        return Core.app

    @staticmethod
    def load_modules(app: Flask, modules_path: str):
        #: Obtenemos el directorio del proyecto
        project_path = path.dirname(path.dirname(__file__))

        #: Recorremos el directorio y sus subdirectorios de forma recursiva e imprimiento de los directorios que estan
        #: dentro de los directorios modules omitiendo todos los directorios que no se llamen modules
        for root, dirs, files in os.walk(modules_path):

            if path.basename(root) == 'modules':
                for module in dirs:

                    #: Exclude modules that start with underscore
                    if module.startswith('_'):
                        continue

                    #: Construimos la ruta del módulo basado para cargarlo dinámicamente en la aplicación
                    module_path = path.join(root, module)
                    module_name = module_path.replace(os.sep, '.')

                    for parts in module_name.split('.'):
                        if parts != 'app':
                            #: remove the first part of the module name
                            module_name = module_name.replace('.', '', 1)
                            module_name = module_name.replace(parts, '', 1)
                        elif parts == 'app':
                            break
                    
                    #: Cargamos el módulo dinámicamente
                    module = __import__(module_name, fromlist=['*'])
                    
                    #: Obtenemos el nombre del módulo
                    module_name = module_name.split('.')[-1]

                    #: Convertimos module_name de snake_case a CamelCase
                    module_name = ''.join(x.capitalize() or '_' for x in module_name.split('_'))                
                    
                    #: Obtenemos el nombre de la clase
                    class_name = module_name + 'View'

                    #: Obtenemos la clase del módulo
                    class_name = getattr(module, class_name)

                    #: Obtenemos la ruta del módulo
                    module_path = module_path.replace(project_path, '')
                    module_path = module_path.replace('modules', '').replace('//', '/')

                    endpoint = module_name.split('/')[-1].lower()

                    #: Agregamos la ruta del módulo a la aplicación
                    module_paths = [
                        [module_path, ['GET', 'POST'], 'main-' + endpoint],
                        [module_path + '/<int:id>', ['GET', 'POST', 'PUT', 'DELETE'], 'main-id' + endpoint],
                        [module_path + '/<int:id>/<string:action>', ['GET', 'POST', 'PUT', 'DELETE'], 'main-id-action' + endpoint],
                    ]

                    for module_path in module_paths:
                        app.add_url_rule(
                            module_path[0],
                            view_func=class_name.as_view(module_path[2]),
                            methods=module_path[1]
                        )
    

    @staticmethod
    def load_dotenv(dotenv_path: str):
        load_dotenv(dotenv_path)


    #: Método que converte valores string en valores booleanos
    @staticmethod
    def str_to_bool(value: str) -> bool:
        return value.lower() in ("yes", "Yes", "true", "True", "t", "1", "on", "On", "y", "Y")
    