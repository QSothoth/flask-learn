# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message=u'用户名不能为空'),
                                           Length(2, 20, message=u'用户名长度不对')],
                       render_kw={"placeholder": "Your name"})
    password = StringField('password', validators=[DataRequired()],
                           render_kw={"placeholder": "password"})
    submit = SubmitField(label=u'login')
