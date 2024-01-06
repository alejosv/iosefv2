# -*- encoding: utf-8 -*-

from flask.views import MethodView
from flask import render_template, request, redirect, url_for, flash, session
from .forms.login import LoginForm

class LoginView(MethodView):

    template_url = __name__.split('.')[2]

    def get(self, id: int = None):
        form = LoginForm()
        if id:
            return 'GET {}'.format(id)
        else:
            return render_template('auth/login.html', title='Login', form=form)
    
    def post(self):
        data = request.form
        form = LoginForm(data=data)
        if form.validate():
            flash('Login exitoso', 'success')
            return redirect(url_for('main-login'))
        else:
            flash('Inicio de sesión fallido', 'danger')
            return redirect(url_for('main-login'))
        return data
    
    def put(self, id: int):
        return 'PUT {}'.format(id)
