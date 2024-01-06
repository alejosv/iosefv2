# -*- encoding: utf-8 -*-

from flask_wtf import Form
from wtforms import PasswordField, validators, EmailField, StringField

class SingUpForm(Form):

    name = StringField('Nombre', [
        validators.DataRequired()
    ])

    email = EmailField('Correo Electrónico',[
        validators.DataRequired(),
        validators.Email()
    ])

    password = PasswordField('Contraseña', [
        validators.DataRequired()
    ])

    confirm_password = PasswordField('Confirmar Contraseña', [
        validators.DataRequired(),
        validators.EqualTo('password', message='Las contraseñas no coinciden')
    ])
