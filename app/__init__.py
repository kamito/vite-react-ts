import json
from base64 import urlsafe_b64encode
from flask import request, session, render_template, redirect, jsonify
from .app import app
from .blocks import blocks, blocks_login

@app.route("/")
@blocks_login
def top():
    data = blocks.login_data
    return render_template(
        "top.html",
        b64_data_json=urlsafe_b64encode(json.dumps(data).encode())
        )
