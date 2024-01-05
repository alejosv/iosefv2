# -*- encoding: utf-8 -*-

from flask.views import MethodView
from flask import render_template


class LoginView(MethodView):

    template_url = __name__.split('.')[2]

    def get(self, id: int = None):
        if id:
            return 'GET {}'.format(id)
        else:
            return render_template('auth/login.html', title='Login')
    
    def post(self):
        return 'POST'
    
    def put(self, id: int):
        return 'PUT {}'.format(id)
