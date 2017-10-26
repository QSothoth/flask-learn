# -*- coding: utf-8 -*-
# hello word
from flask import Blueprint, render_template, redirect , url_for
from .nav import nav
from flask_nav.elements import Navbar, View, Separator, Subgroup, Link
from .forms import LoginForm

main = Blueprint('main', __name__)

# registers the "top" menubar
nav.register_element('index_top', Navbar(
    u'Rorschach',
    View('Blog', 'main.blog'),
    View('About', 'main.about'),
    Subgroup(
        'Products',
        View('login', 'main.login'),
        View('About', 'main.about'),
        Separator(),
        Link('Tech Support', 'http://techsupport.invalid/widgits_inc'),
    ),
    View('About', 'main.about'),
))


@main.route('/')
def index():
    return render_template('index.html', title='Personal Site')


@main.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('main.index'))
    return render_template('login.html', form=form)


@main.route('/blog')
def blog():
    return u'没有blog'


@main.route('/about')
def about():
    return u'没有关于'
