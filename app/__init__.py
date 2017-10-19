# -*- coding: utf-8 -*-
from flask import Flask
from flask_bootstrap import Bootstrap
from .main import main
from .nav import nav


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('default_config.py')
    # 实例化Bootstrap？
    Bootstrap(app)
    print nav
    nav.init_app(app)
    app.register_blueprint(main)
    return app
