#!/usr/bin/env python
import os
import logging
import datetime
from flask import Flask
from whitenoise import WhiteNoise
from .const import FLASK_SECRET_KEY, Const

app = Flask(
    __name__,
    template_folder=os.path.abspath("./app/templates")
    )
app.secret_key = FLASK_SECRET_KEY
app.permanent_session_lifetime = datetime.timedelta(hours=24)

IS_DEBUG = app.config["DEBUG"]

WHITENOISE_MAX_AGE = 31536000 if not IS_DEBUG else 0
whitenoize_base_path = "../frontend" if IS_DEBUG else "../frontend/dist"
whitenoise_root_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), whitenoize_base_path))
app.wsgi_app = WhiteNoise(
    app.wsgi_app,
    root=whitenoise_root_path,
    prefix="",
    max_age=WHITENOISE_MAX_AGE,
    autorefresh=IS_DEBUG
    )

const_o = Const(is_debug=IS_DEBUG)
app.jinja_env.globals.update(const_o.__dict__)
