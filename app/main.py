# -*- coding: utf-8 -*-
# hello word
from flask import Blueprint, render_template
from .nav import nav
from flask_nav.elements import Navbar, View, Separator, Subgroup, Text, Link

main = Blueprint('main', __name__)

# registers the "top" menubar
nav.register_element('index_top', Navbar(
    u'Rorschach',
    View('Blog', 'main.blog'),
    View('About', 'main.about'),
    Subgroup(
        'Products',
        View('Blog', 'main.blog'),
        View('About', 'main.about'),
        Separator(),
        Text('Discontinued Products'),
        View('Blog', 'main.blog'),
        View('About', 'main.about'),
        Link('Tech Support', 'http://techsupport.invalid/widgits_inc'),
    )
))
print nav

@main.route('/')
def index():
    return render_template('index.html', title='Personal Site')


@main.route('/blog')
def blog():
    return u'没有blog'


@main.route('/about')
def about():
    return u'没有关于'
