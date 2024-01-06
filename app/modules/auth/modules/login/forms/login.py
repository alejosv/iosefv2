# -*- encoding: utf-8 -*-

from flask_wtf import Form
from wtforms import PasswordField, validators, EmailField, BooleanField

class LoginForm(Form):
    email = EmailField('Correo Electrónico',[
        validators.DataRequired(),
        validators.Email()
    ])

    password = PasswordField('Contraseña', [
        validators.DataRequired()
    ])

    remember_me = BooleanField('Mantener sesión', [])
