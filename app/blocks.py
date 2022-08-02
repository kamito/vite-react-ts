#!/usr/bin/env python
from urllib.parse import urlparse
from flask import request, session, redirect
from blocks import Blocks
from .app import app, const

blocks = Blocks(
    secret=const.get('BLOCKS_API_SECRET'),
    api_token=const.get('BLOCKS_API_TOKEN')
    )

BLOCKS_SESSTION_DATA_KEY = "__blocks_login_data"


def blocks_login(fn):
    def wrapper(*args, **kwargs):
        if session and BLOCKS_SESSTION_DATA_KEY in session:
            data = session[BLOCKS_SESSTION_DATA_KEY]
            blocks.set_login_data(data)
            return fn(*args, **kwargs)
        else:
            redirect_to = urlparse(request.host_url)
            redirect_to = redirect_to._replace(path="/__loggined")
            rurl = blocks.redirect_login(
                url=const.get('BLOCKS_URL'),
                redirect_to=redirect_to.geturl())
            return redirect(rurl)
    return wrapper


@app.route("/__loggined")
def loggined():
    data = request.args.get('data')
    data = blocks.parse_response_data(data)
    session[BLOCKS_SESSTION_DATA_KEY] = data
    return redirect("/")
