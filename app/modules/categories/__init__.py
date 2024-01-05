# -*- encoding: utf-8 -*-

from flask.views import MethodView
from flask import render_template
from flask_login import login_required


class CategoriesView(MethodView):

    # decorators = [login_required]
    template_url = __name__.split('.')[2]

    def __init__(self) -> None:
        super().__init__()

    
    def get(self, id: int = None, action: str = None):
        if id and action:
            return 'GET {0} {1}'.format(action, id)
        elif id:
            return 'GET {}'.format(id)
        else:
            self.template = '{}/index.html'.format(self.template_url)
            return render_template(self.template)
        
    def post(self):
        return 'POST'
    
    def put(self, id: int):
        return 'PUT {}'.format(id)

