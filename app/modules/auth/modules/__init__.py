# -*- encoding: utf-8 -*-

from flask.views import MethodView




class LoginView(MethodView):
    
    def get(self):
        return 'GET'
    
    def post(self):
        return 'POST'
    
    def put(self):
        return 'PUT'
    
    def delete(self):
        return 'DELETE'
