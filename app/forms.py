# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf          import FlaskForm
from flask_wtf.file     import FileField, FileRequired
from wtforms            import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, DataRequired

class LoginForm(FlaskForm):
    username    = StringField  (u'Username'        , validators=[DataRequired()])
    password    = PasswordField(u'Password'        , validators=[DataRequired()])

class RegisterForm(FlaskForm):
    username    = StringField  (u'Username'  , validators=[DataRequired()])
    password    = PasswordField(u'Password'  , validators=[DataRequired()])
    email       = StringField  (u'Email'     , validators=[DataRequired(), Email()])

class MapForm(FlaskForm):
    date1 = SubmitField('2013')
    date2 = SubmitField('2014')
    
    date3 = SubmitField('2015')
    
    date4 = SubmitField('2016')
    
    date5 = SubmitField('2017')
    
    date6 = SubmitField('2018')
    
    date7 = SubmitField('2019')
