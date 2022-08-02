from flask import request, session, render_template, redirect, jsonify
from .app import app
from .blocks import blocks, blocks_login

@app.route("/")
@blocks_login
def top():
    data = blocks.login_data
    return render_template("top.html")
