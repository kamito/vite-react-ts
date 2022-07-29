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
app.wsgi_app = WhiteNoise(
    app.wsgi_app,
    root=os.path.join(os.path.dirname(__file__), "../frontend"),
    prefix="",
    max_age=WHITENOISE_MAX_AGE,
    autorefresh=IS_DEBUG
    )

app.jinja_env.globals.update(Const.__dict__)
app.jinja_env.globals.update({"IS_DEBUG": IS_DEBUG})
