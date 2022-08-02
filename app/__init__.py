import json
from base64 import urlsafe_b64encode
from flask import request, session, render_template, redirect, jsonify
from .app import app, const
from .blocks import blocks, blocks_login

@app.route("/")
@blocks_login
def top():
    data = blocks.get_data_for_view()
    data['IS_DEBUG'] = const.IS_DEBUG
    data['IS_LOCAL'] = const.IS_LOCAL
    return render_template(
        "top.html",
        b64_data_json=urlsafe_b64encode(json.dumps(data).encode())
        )
