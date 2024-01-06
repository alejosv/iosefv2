# -*- encoding: utf-8 -*-

from flask.views import MethodView
from flask import render_template, request, redirect, url_for, flash, session
from .forms.signup import SingUpForm

class SignupView(MethodView):

    template_url = __name__.split('.')[2]

    def get(self, id: int = None):
        form = SingUpForm()
        if id:
            return 'GET {}'.format(id)
        else:
            return render_template('auth/signup.html', title='Signup', form=form)
    
    def post(self):
        data = request.form
        form = SingUpForm(data=data)
        if form.validate():
            flash('Signup exitoso', 'success')
            return redirect(url_for('main-signup'))
        else:
            flash('Inicio de sesión fallido', 'danger')
            return redirect(url_for('main-signup'))
        return data
    
    def put(self, id: int):
        return 'PUT {}'.format(id)
